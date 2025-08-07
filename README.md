#  AI Merch Maker Lite

An internship project that automates the creation and publishing of AI-generated product listings using Python, JavaScript, Java, and APIs.

---

##  Project Overview

This project simulates an automated eCommerce backend pipeline using:
-  AI-generated product content (title, description, tags, image placeholder)
-  Mockup simulation (via JavaScript and Canvas)
-  Publishing via a fake Spring Boot backend
-  Orchestration using Python

---

##  Technologies Used

| Part                  | Language        | File(s)                                      |
|-----------------------|-----------------|----------------------------------------------|
| Product Generator     | Python          | `generate_product.py`                        |
| Mockup Visualizer     | JavaScript      | `mockup_generator.js`                        |
| Product Publisher API | Java (Spring)   | `PublisherApplication.java`, `ProductController.java` |
| Orchestrator          | Python          | `orchestrator.py`                            |

##  Folder Structure

AI-Merch-Maker-Lite/
├── .env # Environment variables (excluded from GitHub)
├── README.md
├── generate_product.py # Product data generator (Python)
├── caption_image.py # (Optional) Image captioning placeholder
├── orchestrator.py # Main automation script (Python)
├── mockup_generator.js # Mockup generator (JavaScript)
├── mockup_result.json # Mockup response simulation
├── demo/ # Java Spring Boot backend
│ └── src/
│ └── main/
│ └── java/com/example/demo/
│ ├── ProductController.java
│ ├── PublisherApplication.java
│ └── ...
└── pom.xml # Maven build config for Spring Boot
---

##  Sample Output

=======
AI-Merch-Maker-Lite/
├── .env # Environment variables (excluded from GitHub)
├── README.md
├── generate_product.py # Product generator (Python)
├── caption_image.py # (Optional) Image captioning simulation
├── orchestrator.py # Full automation script
├── mockup_generator.js # JavaScript mockup generator
├── mockup_result.json # Output JSON from mockup
├── demo/ # Java Spring Boot backend
│ └── src/
│ └── main/java/com/example/demo/
│ ├── ProductController.java
│ └── PublisherApplication.java
└── pom.xml # Maven config for Spring Boot
---


---

## 🧪 Sample Output

>>>>>>> 8f2f4aa (done)
```json
{
  "title": "Neon Wolf Cap",
  "description": "A cool cap with a glowing wolf graphic inspired by AI.",
  "tags": ["neon", "wolf", "cap", "streetwear", "ai"],

  "image_url": "https://via.placeholder.com/512x512.png?text=Neon+Wolf+Cap",
  "image_url": "https://placehold.co/512x512?text=Neon+Wolf+Cap",
  "mockup": {
    "mockup_id": "mock_123456",
    "product": "T-Shirt",
    "variant": "Black / M",

    "image": "https://via.placeholder.com/512x512.png?text=Neon+Wolf+Cap",
    "mockup_preview": "https://via.placeholder.com/512x512.png?text=Neon+Wolf+Cap&mockup=true",
    "status": "mockup_generated"
  }
}

=======
    "image": "https://placehold.co/512x512?text=Neon+Wolf+Cap",
    "mockup_preview": "https://placehold.co/512x512?text=Neon+Wolf+Cap+Mockup",
    "status": "mockup_generated"
  }
}

---

### 4. Learnings (optional)
```markdown
##What I Learned

- Integrating APIs using Python and JavaScript
- Building REST APIs with Spring Boot (Java)
- Automating pipelines and connecting microservices
- Using Git and GitHub effectively


##  How to Run

###  Start the Java Spring Boot Server

```bash
mvn spring-boot:run


### Bonus AI (Simulated)

- AI-based tags were generated using logic tied to the product name (e.g., “Neon Wolf Cap” → tags like `["neon", "wolf", "cap", "streetwear"]`).
- A full image captioning model was not implemented due to scope, but placeholders and logic are in place to simulate this functionality.


