# This is btc price scraping code

# Start import
import requests as req
from bs4 import BeautifulSoup

# Setting info
url = 'https://coinmarketcap.com/currencies/bitcoin/'
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

# Start scraping
page = req.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Get price
btc_prc = soup.find('div', attrs={'class':'priceValue'}).get_text()

# Print info
print(btc_prc)
