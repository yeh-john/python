# This is coinmarketcap scraping code.

# Start import
import requests as req
from bs4 import BeautifulSoup

# Setting info
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
input_coin = input('Enter coinmarketcap coin name(EX:bitcoin) :')
url = 'https://coinmarketcap.com/currencies/'+input_coin

# Start scraping
page = req.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Get price
coin_prc = soup.find('div', attrs={'class':'priceValue'}).getText()

# Print info
print(input_coin+' price:')
print(coin_prc)
