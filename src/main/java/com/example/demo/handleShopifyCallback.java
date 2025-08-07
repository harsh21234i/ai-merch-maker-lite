package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/shopify")
public class handleShopifyCallback {

    @GetMapping("/callback")
    public String handleCallback(
            @RequestParam String code,
            @RequestParam String hmac,
            @RequestParam String shop,
            @RequestParam String timestamp
    ) {
        return "App installed for shop: " + shop + " with code: " + code;
    }
}
