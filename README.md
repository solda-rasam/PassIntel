# 🔒 PassIntel

**PassIntel** (Password Intelligence Tool) is a lightweight, privacy-focused open-source web application designed to analyze password strength, estimate brute-force cracking timelines, and query real-world data breach leaked databases.

Built with Python (Flask) and modern web technology, it provides deeply detailed cryptographic insights into credentials without compromising user privacy.

---

## ✨ Features

- **🛡️ Privacy-First Breach Check:** Uses the K-Anonymity model via the *HaveIBeenPwned API*. Only the first 5 characters of the SHA-1 password hash are transmitted online, keeping the actual password 100% secure.
- **⏳ Brute-force Calculation:** Computes the exact mathematical probability and estimates how long it would take for a high-performance cracking rig (100 Billion guesses/sec) to crack the password.
- **📊 Shannon Entropy Analysis:** Measures the randomness and bits of strength embedded within the character pool.
- **🎨 Cyberpunk UI:** A responsive, modern, dark-themed dashboard tailored for security enthusiasts.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, Requests, Math, Hashlib
- **Frontend:** Vanilla HTML5, CSS3 (Modern Flexbox Grid), JavaScript (Fetch API)

---

## 🚀 Installation & Local Setup

Get PassIntel up and running on your local machine in less than 2 minutes:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/solda-rasam/PassIntel.git](https://github.com/solda-rasam/PassIntel.git)
   cd PassIntel

```
 2. **Install requirements:**
   ```bash
   pip install flask requests
   
   ```
 3. **Run the Flask Server:**
   ```bash
   python app.py
   
   ```
 4. **Access the application:**
   Open your browser and navigate to http://127.0.0.1:5000.
## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
```

