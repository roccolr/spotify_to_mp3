# import requests
# from dotenv import load_dotenv
# import os
from youtube_search import YoutubeSearch

# load_dotenv()
# KEY = os.getenv("GOOGLE_API_KEY")

def get_query_string(track:str, artist:str) -> str:
    query = "https://www.youtube.com/results?search_query="
    word_list = track + ' ' + artist
    for word in word_list.split(' '):
        print('debug')
        query = query + word + '+'
    
    query = query[0:len(query)-1]
    return query


def query_to_id(track:str, artist:str) -> str:
    # query = get_query_string(track, artist)
    results = YoutubeSearch(track+' '+artist, max_results=10)
    return results.videos[0]["id"]


if __name__=='__main__':
    # print(get_query_string('the show must go on', 'queen'))
    query_to_id('i want to break free', 'queen')