import cv2

def decrypt_image(image_path, password_input):
    img = cv2.imread(image_path)

    # Retrieve stored password
    stored_password_chars = []
    for i in range(20):  
        value = img[0, i, 2]
        if value == 255:  
            break
        stored_password_chars.append(chr(value))

    stored_password = "".join(stored_password_chars)

    # Check password
    if password_input != stored_password:
        return {"error": "Incorrect password!"}

    # Retrieve message length
    msg_length = img[0, 0, 0]

    # Decode message
    message = ""
    n, m, z = 0, 1, 0  
    for _ in range(msg_length):
        message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3

    return {"message": "Decryption successful!", "decrypted_text": message}
