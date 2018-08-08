from openpyxl import Workbook
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
import csv

text = '2C2P'
text = urllib.parse.quote_plus(text)

url = 'https://google.com/search?q=' + text

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
urls = []
for h in soup.find_all('h3'):
    # urls.append(h.find('a').attrs['href'])
    a = h.find('a')
    urls.append(a.attrs['href'])
    temp= h.find('a').attrs['href']
    temp=temp[7:]

# updated=[i.split("&sa", 1)[0] for i in temp]
# print(updated)

with open('input.csv', 'rb') as csvfile:
    inputtext = csv.reader(csvfile)
    print(inputtext)
# wb = Workbook()
# ws = wb.active
# wb.save("E:\sample.xlsx")