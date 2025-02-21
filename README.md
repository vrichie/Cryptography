# Cybersecurity Practical Demonstrations

This project consists of two hands-on cybersecurity demonstrations:
1. **Ransomware Simulation** – Encrypt and decrypt image files using a generated key.
2. **Password Hashing & Cracking** – Hash passwords and attempt to crack weak ones using John the Ripper.

---

## **1. Ransomware Simulation**

### **Folder Structure:**
```
Ransom/
├── encrypt_files.py
├── decrypt_files.py
├── generate_key.py
└── secret.key (Generated automatically)
```

### **Step 1: Install Dependencies**
Make sure you have Python installed, then install the required cryptography library:
```bash
pip install cryptography
```

### **Step 2: Generate Encryption Key**
Run the following command to generate a secret key:
```bash
python generate_key.py
```
This will create a `secret.key` file, which is required for encryption and decryption.

### **Step 3: Encrypt Image Files**
Place some `.jpg` or `.png` files in the `Ransom/` folder, then run:
```bash
python encrypt_files.py
```
**Expected Outcome:** The images will be encrypted and will no longer open properly.

### **Step 4: Decrypt Image Files**
To restore the encrypted files, run:
```bash
python decrypt_files.py
```
**Expected Outcome:** The images will be restored to their original state.

---

## **2. Password Hashing & Cracking Using John the Ripper**

### **Folder Structure:**
```
Passwords/
├── password_hash.py
├── hashp.py
├── hashes.txt
├── rockyou.txt (Wordlist for cracking)
```

### **Step 1: Install John the Ripper**
Install John the Ripper on your system:
```bash
# Linux
sudo apt install john

# MacOS
brew install john

# Windows (Using Chocolatey)
choco install john
```

### **Step 2: Hash a Password (Basic Example)**
Run the Python script to hash a password using SHA-256:
```bash
python hashp.py
```
**Example Script (`hashp.py`):**
```python
import hashlib

password = "password123"
hash_object = hashlib.sha256(password.encode())
print(f"SHA-256 Hash: {hash_object.hexdigest()}")
```
Copy the generated hash and try checking it on online hash lookup databases.
example: [CrackStation](https://crackstation.net/)

### **Step 3: Hash a Password for Cracking**
Run the following script to generate a hash and save it to `hashes.txt`:
```bash
python password_hash.py
```
Copy the generated hash and save it into `hashes.txt`.

### **Step 4: Crack the Hashed Password**
Ensure `rockyou.txt` (password wordlist) is in the same folder, then run:
```bash
john --format=bcrypt --wordlist=rockyou.txt hashes.txt
```
If the password exists in the wordlist, John will crack it.

### **Step 5: View Cracked Password**
To display the cracked password, run:
```bash
john --show hashes.txt
```

---

## **Conclusion**
These demonstrations provide practical insights into cybersecurity threats:
- **Ransomware Simulation:** Shows how attackers encrypt files and demand a ransom.
- **Password Cracking:** Demonstrates the importance of strong passwords by cracking weak hashes.
- **Basic Password Hashing:** Highlights how passwords are stored securely and how weak ones can still be compromised.

Always use strong passwords and never execute unknown scripts on your system!

