import requests

# API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"

# Authentication endpoint
auth_url = "https://account.uipath.com/oauth/token"

# API endpoint to fetch data
data_url = "https://your.uipath.api.endpoint/data"

# Prepare data for authentication request
auth_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

# Authenticate and get token
auth_response = requests.post(auth_url, data=auth_data)
auth_response_json = auth_response.json()

if "access_token" in auth_response_json:
    access_token = auth_response_json["access_token"]
    
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
  
