import requests
import csv

bow = []
lyrics_res = ""

with open('song_list_encoded.csv', 'r', newline='') as f:
    reader = csv.reader(f)

    song_list = []
    # print reader
    for row in reader:
        song_list.append(row[0])

    for song in song_list:
        print(f"Retrieving: {song}")

        lyrics_res = requests.get(
            f"https://api.lyrics.ovh/v1/Eminem/{song}")

        if lyrics_res.status_code == 200:
            lyrics = lyrics_res.json()
            for word in lyrics['lyrics'].split():
                bow.append(word)
        else:
            print(f"Error: {lyrics_res.status_code}")
            continue

with open('bow.csv', 'w') as f:
    for word in bow:
        f.write(word + "\n")
    f.close()
