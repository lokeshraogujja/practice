from bs4 import BeautifulSoup
import requests
resp = requests.get("http://www.srikanthtechnologies.com")

# must install lxml to use xml
soup = BeautifulSoup(resp.text, "html.parser")
for item in soup.find_all("img"):
    print(item)

