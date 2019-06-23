import requests
from parsel import Selector

from bs4 import BeautifulSoup

import time
start = time.time()

found =False
text=input("Enter the website : ")
if text=='https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy':
	print('found')
	found=True
else:
	response = requests.get(text)
	raw_html = response.content
	soup = BeautifulSoup(raw_html, 'html.parser')
	links = soup.select('body p > a')

	new_urls=[]
	while (True):

		
		for link in links:
			print(link)

			link = link.get('href')
			print(link)
			if 'https' not in link:
				link ='https://en.wikipedia.org'+link
			if link=='https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy':
				print('found')
				found = True
				break
			else:	
				print(link)
				response = requests.get(link)
				raw_html = response.content
				soup = BeautifulSoup(raw_html, 'html.parser')
				linkss = soup.select('body p > a')
				for link2 in linkss:
					new_urls.append(link2)
				time.sleep(0.5)	
		links=new_urls
		new_urls=[]			
		if found==True:
			break
	if found==False:
		print('not found')
	end = time.time()
	print("Time taken in seconds : ", (end-start))	
			

				



