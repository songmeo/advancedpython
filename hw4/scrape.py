from bs4 import BeautifulSoup
import requests

url = 'https://www.osta.ee/en/category/computers'

#find total pages
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
pages = int(soup.find("span", {"class": "page-count"}).text)

#all product titles
for i in range(pages + 1):
	tmp = url + '/page-' + str(i)
	page = requests.get(tmp)
	soup = BeautifulSoup(page.text, 'html.parser')
	for i in soup.select('a[data-view-src]'):
		print(i.text)
	#print(tmp)
#print(soup.prettify())
