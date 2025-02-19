from flask import Flask, request, jsonify, render_template
from encrypt import encrypt_image
from decrypt import decrypt_image
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    if "image" not in request.files or "message" not in request.form or "password" not in request.form:
        return jsonify({"error": "Missing required fields"}), 400

    file = request.files["image"]
    message = request.form["message"]
    password = request.form["password"]

    # Save uploaded image
    image_path = "uploaded_image.png"
    file.save(image_path)

    # Encrypt Image
    encrypted_path = encrypt_image(image_path, message, password)

    return jsonify({"message": "Image encrypted successfully!", "image_url": encrypted_path})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    if "image" not in request.files or "password" not in request.form:
        return jsonify({"error": "Missing required fields"}), 400

    file = request.files["image"]
    password_input = request.form["password"]

    # Save uploaded encrypted image
    image_path = "uploaded_encrypted.png"
    file.save(image_path)

    # Decrypt Image
    result = decrypt_image(image_path, password_input)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)  # Runs everything on port 5000
