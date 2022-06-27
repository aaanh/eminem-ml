import requests

lyrics = requests.get('https://api.lyrics.ovh/v1/Eminem/Infinite').json()
print(lyrics['lyrics'])