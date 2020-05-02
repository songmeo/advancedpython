from bs4 import BeautifulSoup
import requests
import json
import re, jq

url = 'https://www.osta.ee/en/category/computers'
data = {}
data['items'] = []
#find total pages
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
pages = int(soup.find("span", {"class": "page-count"}).text)

#all product
for i in range(pages + 1):
	tmp = url + '/page-' + str(i)
	page = requests.get(tmp)
	soup = BeautifulSoup(page.text, 'html.parser')
	offers = soup.find_all("figure", {"class":"offer-thumb"})
	for i in offers:
		image = i.find("figure", {"class":"offer-thumb__image"}).find("a")["data-original"]
		title = i.find("p", {"class":"offer-thumb__title"}).text
		price = i.find(lambda tag:tag.name=="span" and "€" in tag.text).text
		data['items'].append({
			'title': title,
			'price': price,
			'image': image
		})
	
with open('data.json', 'w') as outfile:
	json.dump(data, outfile)
