# DISCLAIMER:
# This script is for testing purposes only. It contains dummy sensitive information
# and is not intended for real use. All "sensitive data" included in this script are
# fake and should not be used in any actual environment. This script is intended to 
# test detection capabilities for sensitive information on a GitHub repository.

import requests
import smtplib

# Dummy passwords
admin_password = "Adm1nP@ss!"

# Dummy credit card number
credit_card_number = "4111111111111111"

# Dummy email address
email_address = "fkevengu@bsp.com.pg"
email_password = "emailP@ss!"

# Dummy SSH private key
ssh_private_key = """
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAKbm9uZS1uYW1lAQIDBAUG
BAsFC2YDAAAAQQDDAgECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwd
Hh8gISIjJCUmJygpKissLS4wMTIzNDU2Nzg5Ojs8PT4/Q0RFRkdISUpL
TU5PUFFSU1RVVldYWVpbXF1eX2BhYmNkZWZnaGlqa2xub3Bxc3R1dnd4
eXl6e3x9fn8AAAAobm9uZS1uYW1lLXJzYTI1NDU2LWNoYQAAAAAAAAAG
-----END OPENSSH PRIVATE KEY-----
"""

# Dummy SSL private key
ssl_private_key = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDPm1JwH6oUp7c3
JqscRquhWfDpQvmsJ9RI3Fi1DRflopKUW6EvwNJHMC8DFmFqMhndJ6TlDRY0+Eo+
Gp9vblMeMUElCuLdbsXArC7GAaObFZwz7mr1Ho8GZaGn+wGvlGDkzjcfr6ZWMCpB
----END PRIVATE KEY-----
"""

# Dummy API endpoint
api_endpoint = "https://api.bsp.com.pg/v1/data"

# Dummy function to simulate email connection
def connect_to_email():
    try:
        server = smtplib.SMTP('smtp.bsp.com.pg', 587)
        server.starttls()
        server.login(email_address, email_password)
        print(f"Successfully connected to email: {email_address}")
        server.quit()
    except Exception as e:
        print(f"Failed to connect to email: {e}")

# Dummy function to simulate user actions
def user_action():
    print(f"User email: {email_address}")
    # Example of using the user's email in a fake API request
    response = requests.post(api_endpoint, json={"email": email_address, "action": "test"})
    if response.status_code == 200:
        print("User action successful")
    else:
        print("User action failed")

# Output dummy sensitive information
print("Admin Password:", admin_password)
print("Database Connection String:", db_connection_string)
print("Credit Card Number:", credit_card_number)
print("Email Address:", email_address)
print("Email Password:", email_password)
print("SSH Private Key:", ssh_private_key)
print("SSL Private Key:", ssl_private_key)

# Test the dummy functions
connect_to_email()
user_action()
