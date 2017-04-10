import requests
import json
import time
from bs4 import BeautifulSoup

def scrape(page):

    url = "http://123hindijokes.com/very-funny-jokes/" + str(page)
    json_list = {}
    code = requests.get(url)
    soup = BeautifulSoup(code.content, "lxml")
    uls = soup.findAll('ul', {'class': 'statusList'})
    count = 1
    for ul in uls:
    	for li in ul.findAll('li'):
    		json_list[count] = li.get_text()
    		count += 1

    with open('jokes.json','w') as f:
    	json.dump(json_list, f, ensure_ascii=False, indent=4)
    print("Scraped Page " + str(page))

page = 0

while True:
	scrape(page % 11 + 1)
	time.sleep(10)
	page += 1

