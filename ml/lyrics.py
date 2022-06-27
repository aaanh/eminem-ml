import requests
import csv

bow = set()
lyrics_res = ""

with open('song_list_encoded.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    
    song_list = set()
    # print reader
    for row in reader:
      song_list.add(row[0])

    for song in song_list:
      print("Retrieving: " + song)
      lyrics_res = requests.get('https://api.lyrics.ovh/v1/Eminem/{song}').json()
      print(lyrics_res)
      try:
        bow.add(lyrics_res['lyrics'].split())
      except:
        print(f"Lyrics not found for {song}")
        continue
    
print(lyrics_res)


