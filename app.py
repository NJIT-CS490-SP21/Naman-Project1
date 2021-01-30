"""This module app.py is for running the Flask web server for this web app"""

from os import getenv
from random import choice
from flask import Flask, render_template
from spotify_api import get_access_token, get_artist_top_tracks, get_song_query_string
from genius_api import get_track_data

app = Flask(__name__)

ARTIST_IDS = [
    '0Y5tJX1MQlPlqiwlOH1tJY', # Travis Scott
    '4yvcSjfu4PC0CYQyLy4wSq', # Glass Animals
    '3MZsBdqDrRTJihTHQrO6Dq', # Joji
    '1Xyo4u8uXC1ZmMpatF05PJ', # The Weeknd
]

@app.route('/')
def index():
    """Return the HTML for root endpoint with random song info"""

    access_token = get_access_token()
    artist_id = choice(ARTIST_IDS)
    top_track_data = get_artist_top_tracks(access_token, artist_id)

    track_name = top_track_data['name']
    artist_name = top_track_data['artists'][0]['name']
    song_query_string = get_song_query_string(track_name, artist_name)
    genius_data = get_track_data(song_query_string)

    return render_template(
        'index.html',
        song_name=track_name,
        artist_name=artist_name,
        song_preview_url=top_track_data['preview_url'],
        lyrics_url=genius_data['url'],
        song_image_url=top_track_data['album']['images'][1]['url'],
        artist_image_url=genius_data['primary_artist']['image_url']
    )

app.run(
    port=int(getenv('PORT', 8080)),
    host=getenv('IP', '0.0.0.0'),
    debug=True
)
