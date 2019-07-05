import requests
from bs4 import BeautifulSoup


link = input("URL: ")


r = requests.get(link)
source = r.text
soup = BeautifulSoup(source, 'html.parser')

title = soup.find("div", "c-midnight-100")
category = title.find("strong").text
print(category)


for i in soup.findAll("div", "grid-data-point"):
	name = i.attrs["data-name"]
	
	
	print(name)