import requests
from bs4 import BeautifulSoup
targeturl=input("enter target url: ")
#targeturl="https://atilsamancioglu.com"
foundLinks=[]

def findLinks(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a"):
        foundlink= link.get("href")
        if foundlink:
            if "#" in foundlink:
                foundlink=foundlink.split("#")[0]
            if targeturl in  foundlink and foundlink not in foundLinks:
                foundLinks.append(foundlink)
                print(foundlink)
                findLinks(foundlink)


findLinks(targeturl)
print(foundLinks)