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
            all_fights = BeautifulSoup(card_info.text, 'html')
            fights = all_fights.find_all('a', class_='b-link')
        
            all_fights = str(fights).split("\n")
            print(all_fights)
        

            j +=1
        i = 0
        all_links = []
        while i < len(all_fights):
            all_fights[i] = all_fights[i].replace('View Matchup  </a>','')
            all_fights[i] = all_fights[i].split("/")[-1].replace('">','')
            all_links.append(all_fights[i])
            i+=2

            
            
            

        slow_pointer = 0
        fast_pointer = 2

        while fast_pointer < len(all_links):
            #print("fight" ,all_links[fast_pointer])
            #print("fighter 1" , all_links[slow_pointer])
            slow_pointer += 1
            #print("fighter 2" , all_links[slow_pointer])

            fast_pointer += 3
            slow_pointer += 2

 
