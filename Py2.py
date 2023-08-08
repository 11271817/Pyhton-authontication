import requests

# API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
username = "your_username"
password = "your_password"

# Authentication endpoint
auth_url = "https://account.uipath.com/oauth/token"

# Prepare data for authentication request
auth_data = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password
}

# Authenticate and get token
response = requests.post(auth_url, data=auth_data)
response_json = response.json()

if "access_token" in response_json:
    access_token = response_json["access_token"]
    # API endpoint to fetch data
    data_url = "https://your.uipath.api.endpoint/data"
    
    # Prepare headers for data request
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # Make data request
    data_response = requests.get(data_url, headers=headers)
    data = data_response.json()
    
    # Process the retrieved data
    print(data)
else:
    print("Authentication failed.")
  
