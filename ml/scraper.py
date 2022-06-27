from hashlib import new
import subprocess
from requests import head
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.azlyrics.com/e/eminem.html")

songs = driver.find_elements(By.XPATH, "//div[@class='listalbum-item']/a")
song_list = []
for s in range(len(songs)):
    song_list.append(songs[s].text)

with open('song_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for s in range(len(song_list)):
        writer.writerow([song_list[s]])

# cleanupWithSed = ".\cleanup.sh"
# subprocess.call(cleanupWithSed, shell=True, cwd="./ml")
