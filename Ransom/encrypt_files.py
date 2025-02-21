from cryptography.fernet import Fernet
import os

# Load the encryption key
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key file not found! Run generate_key() first.")
        exit()

# Encrypt image files
def encrypt_files():
    key = load_key()
    cipher = Fernet(key)

    for file in os.listdir():
        if file.endswith(".jpg") or file.endswith(".png"):
            with open(file, "rb") as f:
                file_data = f.read()
            
            encrypted_data = cipher.encrypt(file_data)
            
            with open(file, "wb") as f:
                f.write(encrypted_data)
            
            print(f"Encrypted: {file}")

if __name__ == "__main__":
    encrypt_files()