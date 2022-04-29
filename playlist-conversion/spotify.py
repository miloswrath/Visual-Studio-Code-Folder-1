# Import required modules
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="df3bec0cc87f4f98820cc95a68eb5301",
                                               client_secret="7dab741f0bd54e86be067b69a13b38e7",
                                               redirect_uri="http://192.168.86.34",
                                               scope="user-library-read"))

urn = 'spotify:playlist:5cx6JSdk0d7LkoOp5Ik974'

tracks = sp.playlist(urn)

print(tracks)

