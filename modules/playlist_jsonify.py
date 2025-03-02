from dotenv import load_dotenv
import os
import requests
import base64
import json
from modules.utils import *


def get_playlists(user_id:str, token:str) -> list:
    endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    result = requests.get(endpoint, headers= headers)
    json_result = json.loads(result.content)
    playlists_list = []
    for item in json_result["items"]:
        playlists_dict = {"name":item["name"], "id":item["id"]}
        playlists_list.append(playlists_dict)
    
    return playlists_list

if __name__ == '__main__':
    token = get_token()
    my_id = "11138807782"

    playlists = get_playlists(my_id, token)

