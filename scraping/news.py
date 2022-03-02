# This is news scraping code

# Start import
import requests as req
from bs4 import BeautifulSoup

# Setting info
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
url = 'https://decrypt.co/news'

# Start scraping
page = req.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Get news
news = soup.find_all('h2')

# Print news
for div in news:
    print(div.text)
