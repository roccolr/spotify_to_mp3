from modules.playlist_jsonify import *
from modules.songs import *
from modules.utils import *

def get_playlists_data(usr_id:str, token:str)->list:
    """
    this function returns a list like [{"playlist_name":"my_fav_songs", "playlist_tracks":[{"name":"killer queen", "artist":"queen"}]}]
    """
    return_list = []
    playlists= get_playlists(usr_id, token)

    for playlist in playlists:
        song_list = get_songs(playlist, token)
        entry = {"playlist_name":playlist["name"], "playlist_tracks":song_list}
        return_list.append(entry)
    
    return return_list

def pretty_data_print(playlist_data:list)->None:
    for playlist in playlist_data:
        playlist_name = playlist["playlist_name"]
        playlist_tracks = playlist["playlist_tracks"]
        print(playlist_name)
        for track in playlist_tracks:
            print(format(f"\t[NAME] - {track['name']} | [ARTIST] - {track['artist']}"))
        print('\n\n')

if __name__ == '__main__':
    token = get_token()
    my_id = "11138807782"
    pretty_data_print(get_playlists_data("11138807782", token))

    
