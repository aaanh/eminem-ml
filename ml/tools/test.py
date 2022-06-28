import requests

song = "Infinite"
bow = []

lyrics = requests.get(f"https://api.lyrics.ovh/v1/Eminem/{song}").json()

for word in lyrics['lyrics'].split():
    bow.append(word)

print(bow)

with open('bow.csv', 'w') as f:
    for word in bow:
        f.write(word + "\n")
    f.close()
