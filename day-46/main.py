from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIFY AUTH
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="acf307680f0940f5876e4ffbcb17caed",
                                               client_secret="e64ac36dfe3240a796cdc11d8af8828a",
                                               redirect_uri="https://example.com",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])

# Asking for Date
# date = input("Which year do you want to travel to? Use YYYY-MM-DD format:")
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_name_spans = soup.find_all("h3", class_="a-no-trucate")
# song_names = [song.getText().strip() for song in song_name_spans]
# print(song_names)