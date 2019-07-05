import requests
from bs4 import BeautifulSoup


def get_names(link):
	r = requests.get(link)
	source = r.text
	soup = BeautifulSoup(source, 'html.parser')

	# Checking if we're on the last page of results or not
	for i in soup.findAll("a", "pagination__named-link"):
		if i.text == "Last »":
			notLast = True
		else:
			notLast = False

	# If we're not on the last page, print names and go to next page
	if notLast == True:
		for i in soup.findAll("div", "product-listing__product-name"):
			name = i.text
			print(name)

		current_page = soup.find("li", "pagination__page-number--current")
		next_page = current_page.find_next_sibling()
		link = next_page.find("a", "pagination__page-number-link")["href"]
		get_names(link)
	
	# If last page, just print names
	else:
		for i in soup.findAll("div", "product-listing__product-name"):
			name = i.text
			print(name)


notLast = False

link = input("URL: ")
get_names(link)