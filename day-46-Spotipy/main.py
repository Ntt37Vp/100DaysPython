from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# SCRAPING BILLBOARD
date = input("Which year do you want to travel to? Use YYYY-MM-DD format:")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_name_spans = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_name_spans]
print(song_names)


# SPOTIFY AUTH
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="eec90ee10886464f8c608ebda5fef9d3",
                                               client_secret="7dbd35679a11408fa30da5114bb2bde4",
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private,",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]
# print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
