package com.example.demo;

import java.util.Map;
import java.util.UUID;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/publish")
public class ProductController {

    @PostMapping
    public Map<String, String> receiveProduct(@RequestBody Map<String, Object> productData) {
        System.out.println("Received product: " + productData);
        return Map.of(
            "status", "success",
            "product_id", "prod_" + UUID.randomUUID()
        );
    }
}
