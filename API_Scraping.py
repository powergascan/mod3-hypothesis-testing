import requests
import json
from bs4 import BeautifulSoup

url="https://webrobots.io/kickstarter-datasets/"
resp=requests.get(url=url)
soup = BeautifulSoup(resp.text, 'html.parser')

All_links=soup.select('''a[href]''')
JSON_links=[i.get("href") for i in All_links if i.get("href").endswith(r"json.gz")]

#this scrapes large aount of files

yes=input("enter y to confirm, or anything else to quit: ")

if yes=="y":
    for i in JSON_links:
        filename=i[-32:]
        if filename.startswith("2016") or filename.startswith("2017"): 
            with requests.get(url=i, stream=True) as response:
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)