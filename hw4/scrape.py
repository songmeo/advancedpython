from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.osta.ee/en/category/computers'
data = {}
data['items'] = []
#find total pages
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
pages = int(soup.find("span", {"class": "page-count"}).text)

#all product titles
for i in range(pages + 1):
	tmp = url + '/page-' + str(i)
	page = requests.get(tmp)
	soup = BeautifulSoup(page.text, 'html.parser')
	offers = soup.find_all('p[offer-thumb]')
	for i in offers:
		children = i.findChildren('p', recursive=True)
		for child in children:
			print(child.text)

with open('data.txt', 'w') as outfile:
	json.dump(data, outfile)
	#print(tmp)
#print(soup.prettify())
