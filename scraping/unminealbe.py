# Import
import requests as req
from bs4 import BeautifulSoup

# Help source https://vaaaaaanquish.hatenablog.com/entry/2017/06/25/202924

# Setting scraping info
url = 'https://unmineable.com/coins/MATIC/address/0x8adA7ab50bA2CBE2bD04A8fFC93adCF1aC34edfF'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

# Always needs code
page = req.get(url, timeout=20, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())     # <--- Prit all page source

# a = soup.find(id="__next").getText()

b = soup.find_all('div', attrs={'class':'big-info-number'})

print(b)


# Help source https://vaaaaaanquish.hatenablog.com/entry/2017/06/25/202924
