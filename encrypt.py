import cv2
import numpy as np

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)

    # Store message length
    msg_length = len(message)
    img[0, 0, 0] = msg_length

    # Encode message into pixels
    n, m, z = 0, 1, 0  
    for char in message:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Store password
    for i, char in enumerate(password):
        img[0, i, 2] = ord(char)

    img[0, len(password), 2] = 255  # End delimiter

    encrypted_path = "static/encryptedImage.png"
    cv2.imwrite(encrypted_path, img)
    
    return encrypted_path
