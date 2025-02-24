import hashlib  # Import the hashlib library for hashing

# Define the password to be hashed
password = "password123"

# Create a SHA-256 hash object and hash the password
hash_object = hashlib.sha256(password.encode())

# Print the resulting hash in hexadecimal format
print(f"SHA-256 Hash: {hash_object.hexdigest()}")
