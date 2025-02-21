from cryptography.fernet import Fernet
import os

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Decrypt image files
def decrypt_files():
    key = load_key()
    cipher = Fernet(key)

    for file in os.listdir():
        if file.endswith(".jpg") or file.endswith(".png"):
            with open(file, "rb") as f:
                encrypted_data = f.read()
            
            decrypted_data = cipher.decrypt(encrypted_data)
            
            with open(file, "wb") as f:
                f.write(decrypted_data)
            
            print(f"Decrypted: {file}")

if __name__ == "__main__":
    decrypt_files()