"""Contains methods related to fetching data via Genius API"""

from os import environ
from requests import get

BASE_URL = 'https://api.genius.com/search'

def get_track_data(song_query):
    """ Given a song + artist query string, search for Genius lyrics page"""

    access_token = environ['GENIUS_ACCESS_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}

    params = {'q': song_query}
    response = get(BASE_URL, params=params, headers=headers)

    data = response.json()
    hits = data['response']['hits']

    def filter_hits(hit):
        return hit['type'] == 'song'

    song_hits = filter(filter_hits, hits)
    return list(song_hits)[0]['result']
