from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

URL_BILLBOARD = "https://www.billboard.com/charts/hot-100/"

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
USERNAME = os.environ["USERNAME"]

# input the date you want
date = input("What date would you like to travel. Type the date in this formate YYY-MM-DD: ")

#######################################################################################
# BILLBOARD request the HTML text
response = requests.get(URL_BILLBOARD + date)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
song_names_tags = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_tags]

#######################################################################################
# SPOTIFY AUTHENTICATION
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

#######################################################################################
# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]  # get just the year

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(json.dumps(result))  # json.dumps() to chance single to double quotes '' -> "" and see in json viewer
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#######################################################################################
# Creating a new playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100 - Jordan", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)