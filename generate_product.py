import random
import json

def generate_product_data():
    titles = [
        "Cyber Cat Tee",
        "Pixel Sunset Hoodie",
        "AI Alien Mug",
        "Glitch Bear T-Shirt",
        "Neon Wolf Cap"
    ]
    descriptions = [
        "A futuristic tee featuring a neon cat designed with AI.",
        "A comfy hoodie with a pixelated sunset artwork.",
        "A ceramic mug showcasing an AI-generated alien face.",
        "T-shirt with a glitched bear print — powered by machine learning.",
        "A cool cap with a glowing wolf graphic inspired by AI."
    ]
    tags_list = [
        ["cyber", "cat", "ai", "tech", "tee"],
        ["sunset", "pixel", "hoodie", "cozy", "retro"],
        ["alien", "mug", "space", "weird", "cool"],
        ["glitch", "bear", "shirt", "ml", "vaporwave"],
        ["neon", "wolf", "cap", "streetwear", "ai"]
    ]

    i = random.randint(0, len(titles) - 1)

    return {
        "title": titles[i],
        "description": descriptions[i],
        "tags": tags_list[i],
        "image_url": f"https://via.placeholder.com/512x512.png?text={titles[i].replace(' ', '+')}"
    }

if __name__ == "__main__":
    product = generate_product_data()
    print(json.dumps(product, indent=2))
