# Rewe specific code
import requests
import lxml
from bs4 import BeautifulSoup
import time

module_name = "rewe"
name = "Rewe_Leipzig"

def the_page_has_products(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'} 
	content = requests.get(url, headers=headers).content
	soup = BeautifulSoup(content,'lxml') # choose lxml parser
	if (len(soup.findAll("div", {"class" : "search-service-basketButtons"})) == 0):
		return False
	else:
		return True

def find_the_highest_valid_page_number(base_url, i1, i2):
	"""
	Finds the highest valid page number in between i1 and i2.
	"""
	if (i1 > i2):
		raise InputError(i1,'>',i2)
	mid = i1 + int((i2 - i1)/2)
	if ((mid - i1) == 0):
		return i1
	else:
		mid_url = base_url + '?page=' + str(mid)
		if (the_page_has_products(mid_url)):
			return find_the_highest_valid_page_number(base_url, mid, i2)
		else:
			return find_the_highest_valid_page_number(base_url, i1, mid)

def urls():
	Rewe_base_urls = (
	'https://shop.rewe.de/c/frische-kuehlung/',
	'https://shop.rewe.de/c/obst-gemuese/',
	'https://shop.rewe.de/c/tiefkuehl/',
	'https://shop.rewe.de/c/nahrungsmittel/',
	'https://shop.rewe.de/c/suesses-salziges/',
	'https://shop.rewe.de/c/kaffee-tee-kakao/',
	'https://shop.rewe.de/c/getraenke/',
	'https://shop.rewe.de/c/wein-spirituosen-tabak/',
	'https://shop.rewe.de/c/drogerie-kosmetik/',
	'https://shop.rewe.de/c/baby-kind/',
	'https://shop.rewe.de/c/kueche-haushalt/',
	'https://shop.rewe.de/c/haus-freizeit/',
	'https://shop.rewe.de/c/garten-outdoor/',
	'https://shop.rewe.de/c/tier/' )
	for base_url in Rewe_base_urls:
		highest_valid_page_number = find_the_highest_valid_page_number(base_url, 1, 200)
		for i in range(1, highest_valid_page_number + 1):
			url = base_url + '?page=' + str(i)
			yield(url)

def process_url(url):
	return url.split('.png')[0]+'.png'
	time.sleep(2)