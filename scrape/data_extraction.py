import string
import os
from importlib import import_module
from bs4 import BeautifulSoup
import requests
import json
from google.cloud import storage
import time

def extract_url_from_srcset(url, resolution):
	split_url = (str(url)).split(',')
	if (resolution == 'low'):
		return split_url[0].split(' ')[0]
	elif (resolution == 'high'):
		return split_url[0].split(' ')[-1]

def retrieve_all_images_on_page(websiteModuleList):
	print("Crawling the following: {}".format(websiteModuleList))
	websiteModules = {}
	for websiteModuleName in websiteModuleList:
		websiteModules[websiteModuleName] = import_module('sources.' + websiteModuleName)
	# generate a list of urls to crawl
	try:
		with open("temp/image_dict.json",'r') as json_file:
			image_dict = json.load(json_file)
		with open("temp/urls_to_crawl.json",'r') as json_file:
			urls_to_crawl = json.load(json_file)
	except:
		urls_to_crawl = {}
		for website in websiteModules.values():
			print("Aggregrating list from {}.".format(website.name))
			for url in website.urls():
				urls_to_crawl[url] = { 'source': website.module_name, 'crawled': False }
		with open("temp/urls_to_crawl.json",'w') as json_file:
			json.dump(urls_to_crawl, json_file)
		image_dict = {}
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'} 
	# necessary since some websites don't allow crawling, oops.
	for url, info in urls_to_crawl.items():
		# check if url has already been retrieved
		if not (info['crawled']):
			print('Retrieving ' + url + '...')
			content = requests.get(url, headers=headers).content
			soup = BeautifulSoup(content,'lxml') # choose lxml parser
			image_tags = soup.findAll('img')
			for image_tag in image_tags:
				if (image_tag.get('alt') != None):
					# is it src or srcset?
					if (image_tag.get('srcset')) is not None:
						lowres_image_url = str(extract_url_from_srcset(image_tag.get('srcset'), 'low'))
					elif (image_tag.get('src')) is not None:
						lowres_image_url = str(image_tag.get('src'))
					else:
						continue
					image_dict[image_tag.get('alt')] = {
						'link' : websiteModules[info['source']].process_url(lowres_image_url),
						'tags' : {
							'0' : 'relevant',
							'1' : websiteModules[info['source']].name
						}
					}
			urls_to_crawl[url]['crawled'] = True
			# save locally
			with open("temp/image_dict.json",'w') as json_file:
				json.dump(image_dict, json_file)
			with open("temp/urls_to_crawl.json",'w') as json_file:
				json.dump(urls_to_crawl, json_file)
			time.sleep(5)
	os.remove('temp/image_dict.json')
	os.remove('temp/urls_to_crawl.json')
	return image_dict

def write(bucket_name, destination_blob_name, data):
	try:
		storage_client = storage.Client()
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(destination_blob_name)
		blob.upload_from_string(data)
		print('File uploaded to {}.'.format(destination_blob_name))
		return True
	except:
		print(err)
		print('Google storage API failed. If you are local, remember to add the security credentials. Reverting to saving locally.')
		with open('image_tags.json','w') as json_file:
			json_file.write(images_json)
	

if __name__ == "__main__":
	# retrieve all the website and their corresponding instruction from '/sources'
	list_of_files = os.listdir('sources')
	list_of_python_files = list(filter(lambda x: x.endswith('.py'), list_of_files))
	list_of_python_file_names = list(map(lambda x: x[:-3], list_of_python_files))
	# start crawl
	dict_to_save = retrieve_all_images_on_page(list_of_python_file_names)
	# dict_to_save = retrieve_all_images_on_page(['ALDI', 'rewe'])
	# convert dict to json
	images_json = str(json.dumps(dict_to_save, indent=4, sort_keys=True))
	# save
	write('project-impossible-ml', 'data/image.json', images_json)

