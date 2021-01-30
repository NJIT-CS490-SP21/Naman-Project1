"""Contains methods related to fetching data via Genius API"""

from os import environ
from random import choice
from requests import get, post

AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_access_token():
    """Fetch Spotify access token via POST request"""

    spotify_client_id = environ['SPOTIFY_CLIENT_ID']
    spotify_client_secret = environ['SPOTIFY_CLIENT_SECRET']

    auth_response = post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': spotify_client_id,
        'client_secret': spotify_client_secret,
    })

    auth_response_data = auth_response.json()
    return auth_response_data['access_token']


BASE_URL = 'https://api.spotify.com/v1/artists/'
PARAMS = {'market': 'US'}

def get_artist_top_tracks(access_token, artist_id):
    """Fetch top tracks of a given artist and return data for 1 of the 10"""

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    response = get(BASE_URL + artist_id + '/top-tracks', headers=headers, params=PARAMS)
    data = response.json()

    return choice(data['tracks'])

def get_song_query_string(song_name, artist_name):
    """Returns query string for Genius API search call"""

    cleaned_song_name = song_name.split('(')[0]
    return cleaned_song_name + ' ' + artist_name
