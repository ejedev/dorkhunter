from bs4 import BeautifulSoup
from googlesearch import search
import requests

print("""
    | |             | |   | |                  | |
  __| |  ___   _ __ | | __| |__   _   _  _ __  | |_   ___  _ __
 / _` | / _ \ | '__|| |/ /| '_ \ | | | || '_ \ | __| / _ \| '__|
| (_| || (_) || |   |   < | | | || |_| || | | || |_ |  __/| |
 \__,_| \___/ |_|   |_|\_\|_| |_| \__,_||_| |_| \__| \___||_|
""")
foundUrls = []
dorkList = ["cat", "id", "article", "page", "bookid"]
selection = int(input("\nPlease select a dork:\n[1] cat\n[2] id\n[3] article\n[4] page\n[5] bookid\n[6] Custom dork\n"))
if selection == 6:
    dork = input("\nPlease enter the dork (ex: for ?id= you would just enter id)\n")
else:
    dork = dorkList[selection-1]
finalDork = "inurl: ?" + dork + "="
searchAmount = int(input("\nPlease enter an amount of links to test:\n"))
print("\nSearching and testing...\n")
for x in search(finalDork, tld='com', lang='en', num=searchAmount, start=0, stop=searchAmount, pause=2.0):
    url = x + "'"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    for y in text:
        if y.find("You have an error in your SQL") != -1:
            foundUrls.append(x)
            print("\nVulnerable site found:", x)
file = open("output.txt", "a")
for x in foundUrls:
    file.write(x + "\n")
file.close()
print("\nAll vulnerable sites have been written to output.txt in the root folder.")
