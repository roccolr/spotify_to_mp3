from modules.utils import *
from modules.spotifile import *
from modules.video_to_mp3 import *
import sys

if __name__ == '__main__':

    try: 
        output_path = sys.argv[1]
        id = sys.argv[2]
        # destination = "/home/jsorel/mp3izer/music"
        token = get_token()
        data = get_playlists_data(id, token)
        pretty_data_print(data)
        print("gathering data...")
        id_list=get_id_list(data)
        print("downloading...")
        for id in id_list:
            download_mp3_preserve(data, output_path)
        print("THE END")
    except IndexError:
        print("Please specify output directory path and spotify_id")
    