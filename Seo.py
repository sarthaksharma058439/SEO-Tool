from urllib.request import urlopen
from bs4 import BeautifulSoup

url=input("which page would you like to check?Enter fulll url :")
keyword=input("whta is your seo keyword?")

try:
    html=urlopen(url)
except HTTPError as e:
    print(e)

data = BeautifulSoup(html,"html.parser")

def seo_title(keyword,data):
    if keyword.casefold() in data.title.text.casefold():
        status="found"

    else:
        status="not found"

    return status

print(seo_title(keyword,data))
