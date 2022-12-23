# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:22:49 2022

@author: Cemal
"""

import requests
r = requests.get("https://www.foxsports.com/soccer/2022-fifa-world-cup/standings")
#print(r.text[:500])

bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find_all("tr")
#print(results[0:3])

first_result = results[1]

#cleaning
results = results[:-12]
del results[0], results[4], results[8], results[12], results[16], results[20], results[24], results[28]
print(len(results)) 

# Country Name
name = first_result.find("a", attrs={"class": "table-entity-name ff-s"}).text
print(name)
#Matches played
mp = first_result.find("td", attrs = {"data-index": "2"})
print(mp.contents[1])
mp = mp.contents[1]

# Win Draw Loss
wdl = first_result.find("td", attrs = {"data-index": "3"})
print(wdl.contents[1])
wdl = wdl.contents[1]

# Goals For
gf = first_result.find("td", attrs = {"data-index": "4"})
gf = gf.contents[1]
print(gf)

# Goals Against
ga = first_result.find("td", attrs = {"data-index": "5"})
ga = ga.contents[1]
print(ga)

# Goal Difference
gd = first_result.find("td", attrs = {"data-index": "6"})
gd = gd.contents[1]
print(gd)
# Points
pts = first_result.find("td", attrs = {"data-index": "7"})
pts = pts.contents[1]
print(pts)

# loop
all_countries = []
for result in results:
    Name = result.find("a", attrs={"class": "table-entity-name ff-s"}).text
     
    Mp = result.find("td", attrs = {"data-index": "2"}).text
    
    Wdl = result.find("td", attrs = {"data-index": "3"}).text
    
    Gf = result.find("td", attrs = {"data-index": "4"}).text
   
    Ga = result.find("td", attrs = {"data-index": "5"}).text
    
    Gd = result.find("td", attrs = {"data-index": "6"}).text
    
    Pts = result.find("td", attrs = {"data-index": "7"}).text
   
    all_countries.append((Name, Mp, Wdl, Gf, Ga, Gd, Pts))
    
print(len(all_countries))

# converting into csv file
import pandas as pd
df = pd.DataFrame(all_countries, columns=["Country_Name", "MP", "W-D-L", "GF", "GA", "GD", "PTS"])
df.to_csv("worldcup_fixture.csv", index=False)




