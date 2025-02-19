
# 🔒 PixelCipher

A **web-based image encryption & decryption** system that allows users to **securely encode and decode messages** inside images using password protection.

## 🚀 Features
✅ **Password-Protected Encryption** - Securely hides messages inside images.  
✅ **Fast Image Decryption** - Extracts hidden messages with the correct password.  
✅ **Modern Dark-Themed UI** - Sleek, intuitive web interface.  
✅ **Flask Backend** - Lightweight and efficient server-side processing.  
✅ **No External Database Needed** - Works with just Python & OpenCV.  

---

## 📂 Project Structure
```
/image-encryption-project
│── encrypt.py          # Handles encryption logic
│── decrypt.py          # Handles decryption logic
│── app.py              # Runs the Flask server (Main entry point)
│── templates/
│   └── index.html      # Frontend Web UI (Encryption & Decryption)
│── static/
│   ├── style.css       # Styling (Dark Themed UI)
│   ├── script.js       # Frontend JavaScript (Handles API calls)
│── README.md           # Project Documentation

```

---

## ⚙️ Setup Instructions

### 🔹 **1. Install Required Dependencies**
Ensure Python and required libraries are installed:
```sh
pip install flask opencv-python numpy
```

### 🔹 **2. Run the Flask Server**
```sh
python app.py
```
This starts the server at **http://127.0.0.1:5000/**.

### 🔹 **3. Open the Web Interface**
- Open `index.html` in a browser.
- Select an **image**, enter a **message** & **password**, and click **"Encrypt"**.
- Download the **encrypted image**.
- To decrypt, upload the **encrypted image**, enter the **correct password**, and click **"Decrypt"**.

---

## 📍 Where Are the Encrypted Images Stored?
📌 The **original uploaded image** is stored temporarily.  
📌 The **encrypted image** is saved at:  
   ```
   /static/encryptedImage.png
   ```
📌 The **decrypted message** is displayed on the UI.  

---

## 🔧 Future Enhancements
🚀 **AES Encryption for Stronger Security**  
🚀 **Cloud Storage for Encrypted Images**  
🚀 **Steganography Features for Advanced Data Hiding**  
🚀 **Mobile App Version for Instant Encryption & Decryption**  

---

## 📌 Author & License
🔹 **Created by:** Deeksha J
🔹 **License:** MIT  
🔹 **GitHub Repository:** https://github.com/Deekshagj/PixelCipher.git




