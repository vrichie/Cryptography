import hashlib

password = "password123"
hash_object = hashlib.sha256(password.encode())
print(f"SHA-256 Hash: {hash_object.hexdigest()}")
