package com.example.demo;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController {

    // Home endpoint to test backend
    @GetMapping("/")
    public String home() {
        return " Spring Boot backend is up!";
    }

    // Shopify OAuth callback endpoint
    @GetMapping("/auth/callback")
    public String authCallback(@RequestParam String code,
                               @RequestParam String shop,
                               @RequestParam String hmac,
                               @RequestParam String timestamp) {
        try {
            String clientId = "df452f1d5f0f93b3a6993d9fb5535edf"; //  Replace with your actual Client ID
            String clientSecret = "217f555ef8ce4fe1df34531ee1b78dde"; //  Replace with your actual Client Secret

            String accessTokenUrl = "https://" + shop + "/admin/oauth/access_token";

            String jsonPayload = String.format("""
                {
                  "client_id": "%s",
                  "client_secret": "%s",
                  "code": "%s"
                }
                """, clientId, clientSecret, code);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(accessTokenUrl))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
                    .build();

            HttpClient client = HttpClient.newHttpClient();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            return " Access Token Response:<br><pre>" + response.body() + "</pre>";

        } catch (Exception e) {
            return " Error: " + e.getMessage();
        }
    }
}
