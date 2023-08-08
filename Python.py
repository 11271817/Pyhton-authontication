from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Store the token securely (this is just an example)
token_store = {}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.json['username']
    password = request.json['password']

    # Perform authentication with UiPath and get the token
    auth_data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }
    response = requests.post('UiPath_Authentication_URL', data=auth_data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        token_store[username] = token
        return jsonify({'message': 'Authentication successful'}), 200
    else:
        return jsonify({'message': 'Authentication failed'}), 401

@app.route('/access_data', methods=['GET'])
def access_data():
    username = request.args.get('username')
    token = token_store.get(username)
    
    if not token:
        return jsonify({'message': 'Token not found'}), 401

    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get('UiPath_Data_URL', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Failed to access data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
