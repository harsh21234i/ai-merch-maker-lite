import subprocess
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

if not SHOPIFY_ACCESS_TOKEN or not SHOPIFY_STORE_URL:
    print("❌ Missing Shopify credentials in .env file.")
    exit()

# Step 1: Generate product
print("📦 Generating product...")
gen_result = subprocess.run(
    ["python", "generate_product.py"],
    capture_output=True,
    text=True
)

if gen_result.returncode != 0:
    print("❌ Failed to generate product.")
    print(gen_result.stderr)
    exit()

try:
    product_data = json.loads(gen_result.stdout)
except json.JSONDecodeError:
    print("❌ Invalid JSON from generator.")
    print(gen_result.stdout)
    exit()

print("✅ Product generated:", product_data["title"])

# Step 2: Generate mockup
print("🖼️ Generating mockup...")
title_for_image = product_data["title"]
mockup_result = subprocess.run(
    ["node", "mockup_generator.js", title_for_image],
    capture_output=True,
    text=True
)

if mockup_result.returncode != 0:
    print("❌ Mockup generator failed.")
    print(mockup_result.stderr)
    exit()

# Step 3: Load mockup result
if not os.path.exists("mockup_result.json"):
    print("❌ mockup_result.json not found.")
    exit()

with open("mockup_result.json", "r") as f:
    mockup_data = json.load(f)

print("✅ Mockup generated:", mockup_data["mockup_id"])

# Step 4: Add final image URL (real image override)
product_data["image_url"] = "https://i.ibb.co/cKJFXhmN/wolf.webp"  # Replace if needed

# Step 5: Final payload to backend
final_payload = {
    **product_data,
    "mockup": mockup_data
}

# Step 6: Send to Java backend
print("🚀 Publishing to backend...")
response = requests.post("http://localhost:9090/publish", json=final_payload)

if response.status_code == 200:
    print("✅ Published successfully:", response.json())
else:
    print("❌ Backend error:", response.status_code)
    print(response.text)

# Step 7: Send product to Shopify
print("🛒 Sending product to Shopify...")
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
}

shopify_payload = {
    "product": {
        "title": product_data["title"],
        "body_html": product_data["description"],
        "tags": ", ".join(product_data["tags"]),
        "images": [
            {"src": product_data["image_url"]}
        ]
    }
}

shopify_url = f"https://{SHOPIFY_STORE_URL}/admin/api/2023-04/products.json"
shopify_response = requests.post(shopify_url, headers=headers, json=shopify_payload)

if shopify_response.status_code == 201:
    print("✅ Product published on Shopify!")
    print(json.dumps(shopify_response.json(), indent=2))
else:
    print("❌ Shopify publish failed:")
    print(shopify_response.status_code)
    print(shopify_response.text)
