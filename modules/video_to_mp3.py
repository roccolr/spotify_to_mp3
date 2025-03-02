from modules.ytquery_to_id import *
from pytubefix import YouTube
import os

def get_id_list(data:list)->list:
    id_list = []
    for entry in data:
        for track in entry["playlist_tracks"]:
            # text = track["name"] + track["artist"]
            id_list.append(query_to_id(track=track["name"], artist=track["artist"]))
    return id_list

def download_mp3(id:str, dest:str):
    url = f"https://www.youtube.com/watch?v={id}"
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path=dest)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

def download_mp3_preserve(data:list, dest:str):
    for entry in data:
        id_list = []
        os.mkdir(dest+f'/{entry["playlist_name"]}')
        for track in entry["playlist_tracks"]:
            # text = track["name"] + track["artist"]
            id_list.append(query_to_id(track=track["name"], artist=track["artist"]))
        for id in id_list:
            download_mp3(id, dest+f'/{entry["playlist_name"]}')



