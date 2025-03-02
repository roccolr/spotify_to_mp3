
import requests
import base64
import json
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
secret_id = os.getenv('SECRET_ID')


def get_token() -> str:
    auth_string = os.getenv('CLIENT_ID')+':'+os.getenv('SECRET_ID')
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')


    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Authorization" : "Basic "+auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type":"client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)

    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}

