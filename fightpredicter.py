import requests
from bs4 import BeautifulSoup
import time


url = 'http://ufcstats.com/statistics/events/completed?page=all'
page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.text, 'html')


event_details = soup.find_all('a', class_='b-link')
#print(event_details)

j = 0
for event_link in event_details:
    while j < 1:
        if event_details != None:
            isolated_link = str(event_link).split("/")[-2]
            isolated_link = isolated_link.split('"')[0]
        #print(isolated_link)
            card_info = requests.get('http://ufcstats.com/event-details/{}'.format(isolated_link))
       # for fight in card_info:
            all_links = BeautifulSoup(card_info.text, 'html')
            all_fighters = all_links.find_all('a', class_='b-link')
            #print(all_fighters)


            all_fighters = str(all_fighters).replace("</a>","").split(",")
            print(all_fighters)

            for line in all_fighters:
                line = line.split("/")[-1].replace('">',"").strip()

                print(line[0:16])

            #all_fights = all_links.find_all('a', class_='b-flag')
            #print(all_fights)


            

            j +=  1



