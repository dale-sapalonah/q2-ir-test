# Dummy code for testing sensitive information exposure
# This code is intended for testing purposes only and should not be used in a production environment.

# DISCLAIMER: All data provided below are randomly generated and any conflicts with actual data is coincidental
# Do not use this in production


import requests
import smtplib

# Dummy API keys
api_key_1 = "1234567890abcdef1234567890abcdef"
api_key_2 = "abcdef1234567890abcdef1234567890"

# Dummy passwords
db_password = "P@ssw0rd!"
admin_password = "Adm1nP@ss!"

# Dummy JWT secret
jwt_secret = "supersecretkey"

# Dummy database connection string
db_connection_string = "postgresql://username:password@localhost:5432/mydatabase"

# Dummy credit card number
credit_card_number = "4111111111111111"

# Dummy email address
email_address = "zemo@bsp.com.pg"
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

# Dummy function to access sensitive data
def access_sensitive_data():
    response = requests.get(api_endpoint, headers={"Authorization": f"Bearer {api_key_1}"})
    if response.status_code == 200:
        print("Successfully accessed sensitive data")
    else:
        print("Failed to access sensitive data")

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

# Output dummy sensitive information
print("Dummy sensitive information:")
print("API Key 1:", api_key_1)
print("API Key 2:", api_key_2)
print("Database Password:", db_password)
print("Admin Password:", admin_password)
print("JWT Secret:", jwt_secret)
print("Database Connection String:", db_connection_string)
print("Credit Card Number:", credit_card_number)
print("Email Address:", email_address)
print("Email Password:", email_password)
print("SSH Private Key:", ssh_private_key)
print("SSL Private Key:", ssl_private_key)

# Test the dummy functions
access_sensitive_data()
connect_to_email()
