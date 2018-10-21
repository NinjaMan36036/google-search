from lxml import html
import requests
import os
import datetime
from googlesearch import search

class Gsearch:
	def __init__(self):
		pass
		
	def run(self, query):
		# to search 
		#query = "Geeksforgeeks"
  
		for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
			print(j) 
                x = input('Press enter to continue --> ')
		

class scrape:
    def __init__(self, url):
        print('\nGetting site code from ' + url + ' ... ')
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

    def run(self):
        title = self.titles()
        link = self.links()

    #returns array of titles
    def titles(self):
        print('Scraping titles ... ')
        return self.tree.xpath('//div[@class="wd_title"]/a/text()')

    #returns an array of links
    def links(self):
        print('Scraping links ... ' )
        hrefs = self.tree.xpath('//div[@class="wd_title"]/a')
        ans = []
        for href in hrefs:
            ans.append(href.attrib['href'])
        return ans

    #returns an array of p elements
    def content(self):
        print('Scraping article content ... ')
        temp = self.tree.xpath('//div[@class="wd_body wd_news_body"]/p/text()')
        return temp
		
temp = Gsearch()
temp.run('yeet')
