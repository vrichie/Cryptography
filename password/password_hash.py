import bcrypt  # Import bcrypt for secure password hashing

def hash_password(password):
    """
    Hash a password using bcrypt with a random salt
    Args:
        password: The plain text password to hash
    Returns:
        bytes: The hashed password with salt
    """
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed = bcrypt.hashpw(password.encode(), salt)  # Hash password with salt
    return hashed

def verify_password(password, hashed):
    """
    Verify if a password matches its hash
    Args:
        password: The plain text password to check
        hashed: The stored hash to compare against
    Returns:
        bool: True if password matches, False otherwise
    """
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    # Get password from user input
    password = input("Enter a password to hash: ")
    # Hash the password and store result
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")
    
    # Verify the password by asking user to re-enter it
    test_password = input("Re-enter password to verify: ")
    if verify_password(test_password, hashed_password):
        print("Password matches!")
    else:
        print("Incorrect password!")