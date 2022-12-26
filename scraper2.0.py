# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:47:02 2022

@author: aysen
"""

def get_Name(team):
    name = team.find("a", attrs={"class": "table-entity-name ff-s"}).text
    return name


def get_feature(team, feature):
    if feature == "MP":
        f = "2"
    if feature == "WDL":
        f = "3"
    if feature == "GF":
        f = "4"
    if feature == "GA":
        f = "5"
    if feature == "GD":
        f = "6"
    if feature == "PTS":
        f = "7"
        
    return   team.find("td", attrs = {"data-index": f}).text
        
import requests
r = requests.get("https://www.foxsports.com/soccer/2022-fifa-world-cup/standings")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find_all("tr")


#only getting the teams' information
teams = results
teams = teams[:-12]

i = 0
while i < len(teams):
    if i % 4 == 0:
        del teams[i]
    i +=1


data = []
for team in teams:
    name = get_Name(team)
    mp = get_feature(team, "MP")
    wdl = get_feature(team, "WDL")
    gf = get_feature(team, "GF")
    ga = get_feature(team, "GA")
    gd = get_feature(team, "GD")
    pts = get_feature(team, "PTS")
    data.append((name, mp, wdl, gf, ga, gd, pts))




# converting into csv file
import pandas as pd
df = pd.DataFrame(data, columns=["Country_Name", "MP", "W-D-L", "GF", "GA", "GD", "PTS"])
df.to_csv("worldcup_fixture.csv", index=False)

