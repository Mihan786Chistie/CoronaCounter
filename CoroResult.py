#Project by Syed Md Mihan Chistie
import requests
from bs4 import BeautifulSoup
import bs4
import time
P =[]
A = []
URL = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(URL.content, "html.parser")
h_data = soup.find_all("table", {"id" : "main_table_countries_today"})
print("Welcome To CoronaCounter!!")
print()
cases = soup.find("div", {"class" : "maincounter-number"}).text.strip()
print("Cases: "+str(cases))
print()
act = soup.find("div", {"class": "number-table-main"}).text.replace(",","")
print("Active Cases: "+str(act))
print()
recov = soup.find("div", {"style": "color:#8ACA2B "}).text.replace(",","").strip()
print("Recovered Cases: "+str(recov))
print()
mild = soup.find("span", {"style": "color:#8080FF"}).text
print("Mild Cases: "+str(mild))
print()
recnews = soup.find("li", {"class": "news_li"}).text.replace("[source]", "")
print("Recent News: "+str(recnews))
print()
place = soup.find("a", {"class": "mt_a"}).text
aff = soup.find("td", {"style": "font-weight: bold; text-align:right"}).text
actmo = soup.find("td", {"style": "text-align:right;font-weight:bold;"}).text
recp = (int(recov)/int(act))*100
print("Recovery Percentage: "+str(recp)+" %")
print()
print("Country with Highest Coronavirus Cases: "+str(place)+", with Coronavirus Rate: "+str(aff)+", with Active Cases:"+str(actmo))
print()
print("Country, Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered, Active Cases, Serious, Top Cases")
print()
h_data = h_data[0]
for row in h_data.find_all('tr'):
    for cell in row.find_all('td'):
        allplace = (str(cell.text))
        P.append(allplace)


l = len(P)
c=0
try:
    for k in range(0, l, 1):
       P[k] = P[k].strip()
       for y in range(c, c+12, 1):
           print(P[y], end=" " + "\t")
        
       print()
       c=y
except:
    pass
print()
print("Thanks For Visiting CoronaCounter!!!!!!")
print("Project by Syed Md Mihan Chistie")

