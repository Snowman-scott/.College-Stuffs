import base64
import json
import re

import requests

song_name = "Across The Road"
song_artist = "First of October"
song_album = "Across The Road"
search_req = requests.get(
    f"https://hund.qqdl.site/search/?s={song_name}&a={song_artist}&al={song_album}"
)
search_data = search_req.json()["data"]
data = search_req.json()
print(data)

song_id = search_data["items"][0]["id"]

song_request = requests.get(f"https://hund.qqdl.site/trackManifests/?id={song_id}")

song_request_data = song_request.json()["data"]

print(song_request_data)

url = song_request_data["data"]["attributes"]["uri"]

print(url)
