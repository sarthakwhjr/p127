from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["V Mag. (mV)"	"Proper name"	"Bayer designation"	"Distance (ly)"	"Spectral class"	"Mass (M☉)"	"Radius (R☉)"	"Luminosity (L☉)"]
    planet_data = []
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for trtag in soup.find_all("tr", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        th_tags = trtag.find_all("th")
        temp_list = []
        for index, t_tag in enumerate(th_tags):
            if index == 0:
                temp_list.append(t_tag.find_all("th")[0].contents[0])
            else:
                try:
                    temp_list.append(t_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
  
    with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()