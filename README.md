# 🔐 Secure Token Generator

A user-friendly web application built with Streamlit to generate secure tokens for APIs, authentication, and session management.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- Customizable token length (8-128 characters)
- Flexible character type selection:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&\*)
- Cryptographically secure random generation
- Real-time entropy calculation
- Clean and intuitive user interface
- Token property analysis

## 🛠️ Usage

1. Adjust the token length using the slider
2. Select desired character types:
   - Toggle uppercase letters
   - Toggle lowercase letters
   - Toggle numbers
   - Toggle special characters
3. Click "Generate Token"
4. Copy your secure token
5. View token properties and entropy calculation

## 🔒 Security Features

- Uses Python's `secrets` module for cryptographically secure random generation
- Configurable character set for enhanced security
- Entropy calculation to assess token strength
- No token storage or logging

---

Made with ❤️ by [Your Name]
