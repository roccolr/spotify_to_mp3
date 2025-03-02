from modules.playlist_jsonify import *
from modules.utils import *

def get_songs(playlist:dict, token:str)->list:
    playlist_id = playlist["id"]
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=50&offset=0"
    headers = get_auth_header(token)

    result = requests.get(endpoint, headers=headers)
    result_json = result.json()
    # print(result_json["items"])
    song_list = []
    for item in result_json["items"]:
        song_dict = {"name":item["track"]["name"], "artist": item["track"]["artists"][0]["name"]}
        # print("nome: "+ item["track"]["name"] + " | artista: "+item["track"]["artists"][0]["name"])
        song_list.append(song_dict)
    return song_list

if __name__ == '__main__':
    id = "65tdKed66jdhPSpwpsXKYr"
    token = get_token()
    songlist = get_songs({"id":id}, token)
    print(songlist)