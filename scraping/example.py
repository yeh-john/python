# This is test scraping
# Video source https://youtu.be/UXVvEUYs3KA

import requests as req
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/bitcoin/'

# You can serch internet 'my user agent'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

page = req.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)  # Prit all page source
# title = soup.find(id="__next").get_txt()
# print(title.strip())

# You can't use find_all to getText !!
b = soup.find('div', attrs={'class':'priceValue'}).get_text()  # select div and chouse priceValue

print(b)
