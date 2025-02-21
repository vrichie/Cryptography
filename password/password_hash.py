import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    password = input("Enter a password to hash: ")
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")
    
    test_password = input("Re-enter password to verify: ")
    if verify_password(test_password, hashed_password):
        print("Password matches!")
    else:
        print("Incorrect password!")