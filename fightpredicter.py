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
            #print(all_fighters)

            fighter_stat_links = []
            for line in all_fighters:
                line = line.split("/")[-1].replace('">',"").strip()
                line = line[0:16]
                fighter_stat_links.append(line)
            print(fighter_stat_links)

               
            i = 0
            counter = 0
            for line in fighter_stat_links:
                
                fighter_info = requests.get('http://ufcstats.com/fighter-details/{}'.format(line))
                fighter_info_page = BeautifulSoup(fighter_info.text, 'html')
                Stats = fighter_info_page.find_all('li', class_='b-list__box-list-item')
                Stats = str(Stats).replace('      </li>, <li class="b-list__box-list-item b-list__box-list-item_type_block">', "")
                Stats = str(Stats).replace('<i class="b-list__box-item-title b-list__box-item-title_font_lowercase b-list__box-item-title_type_width">', "")
                Stats = str(Stats).replace(''' </li>, <li class="b-list__box-list-item b-list__box-list-item_type_block">''', "")
                Stats = str(Stats).replace('</li>, <li class="b-list__box-list-item b-list__box-list-item_type_block">', "")
                Stats = str(Stats).replace('<i class="b-list__box-item-title b-list__box-item-title_type_width">', "")
            
                Stats = str(Stats).replace('</i>', "")
                Stats = str(Stats).replace('''<i class="b-list__box-item-title b-list__box-item-title_type_width">''', "")
                Stats = Stats.replace("' ", "")
                Stats = Stats.replace("\n",'').split()[3:-1]
                #print(line)
                #print([str(Stats.index(x)) + x for x in Stats])
                print(Stats)
                if Stats != []:
                    print(Stats[1],Stats[3],Stats[6],Stats[8],Stats[12],Stats[17],Stats[22],Stats[28],Stats[31])
                    counter += 1
                
                i += 1

            print(counter)
            
            j +=  1




