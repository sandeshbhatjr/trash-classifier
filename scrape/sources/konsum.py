# Konsum specific code
import requests
import lxml
from bs4 import BeautifulSoup
import time

module_name = "konsum"
name = "konsum_leipzig"

def the_page_has_products(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'} 
	content = requests.get(url, headers=headers).content
	soup = BeautifulSoup(content,'lxml') # choose lxml parser
	if (len(soup.findAll("div", {"class" : "product--box"})) == 0):
		return False
	elif (len(soup.findAll("div", {"class" : "product--box"})) > 0):
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
		mid_url = base_url + str(mid)
	if (the_page_has_products(mid_url)):
		return find_the_highest_valid_page_number(base_url, mid, i2)
	else:
		return find_the_highest_valid_page_number(base_url, i1, mid)

def urls():
	base_url = 'https://www.konsum-leipzig.de/online-bestellen/alle-produkte/?p='
	highest_valid_page_number = find_the_highest_valid_page_number(base_url, 1, 500)
	for i in range(1, highest_valid_page_number + 1):
		url = base_url + str(i)
		yield(url)

def process_url(x):
	time.sleep(2)
	return x
