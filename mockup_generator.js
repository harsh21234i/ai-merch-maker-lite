// mockup_generator.js
const fs = require('fs');

const title = process.argv[2] || "Default Image";
const encodedText = encodeURIComponent(title);

const imageUrl = `https://placehold.co/512x512?text=${encodedText}`;
const previewUrl = `https://placehold.co/512x512?text=${encodedText}+Mockup`;

const mockupData = {
  mockup_id: "mock_" + Math.floor(Math.random() * 1000000),
  product: "T-Shirt",
  variant: "Black / M",
  image: imageUrl,
  mockup_preview: previewUrl,
  status: "mockup_generated"
};

fs.writeFileSync("mockup_result.json", JSON.stringify(mockupData, null, 2));
console.log(" Mockup generated and saved to mockup_result.json");
