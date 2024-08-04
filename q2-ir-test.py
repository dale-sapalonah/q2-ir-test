# Dummy code for testing sensitive information exposure
# This code is intended for testing purposes only and should not be used in a production environment.

# Example of sensitive information stored in variables
api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Dummy API key
db_password = "password1234"  # Dummy database password
email_password = "emailPass!2024"  # Dummy email account password
admin_email = "zemo@bsp.com.pg" #Dummy email user for fake user

# Fake API endpoints
api_endpoint = "https://api.bsp.com.pg/v1/resource"  # Dummy API endpoint
login_url = "https://bsp.com.pg/login"  # Fake login endpoint
data_url = "https://bsp.com.pg/data"  # Fake data access endpoint

def connect_to_database():
    # Function to simulate connecting to a database with sensitive info
    print("Connecting to database with the following credentials:")
    print(f"API Key: {api_key}")
    print(f"Database Password: {db_password}")

def send_email():
    # Function to simulate sending an email with sensitive info
    print("Sending email with the following credentials:")
    print(f"Email Password: {email_password}")
    print(f"User Email: {admin_email}")

def fetch_data():
    # Function to simulate fetching data from a fake API endpoint
    import requests
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(data_url, headers=headers)
    print(f"Fetched data from {data_url} with status code {response.status_code}")

if __name__ == "__main__":
    connect_to_database()
    send_email()
    fetch_data()
