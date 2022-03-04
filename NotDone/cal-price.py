# This calculator can calculate input_token amount to usd.

# Start import
from bs4 import BeautifulSoup
import requests as req
import re

# Setting info
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
input_token = input('Enter coinmarketcap coin name(EX:bitcoin) :')
url = 'https://coinmarketcap.com/currencies/'+input_token

# Start scraping
page = req.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Get info
token_prc = soup.find('div', attrs={'class':'priceValue'}).getText()
symbol = soup.find('small', attrs={'class':'nameSymbol'}).getText()

# Print current token price
print(symbol+' current price')
print(token_prc)

# Ask how many token do you have
token_amt = input('Enter '+symbol+' amount :')

# Ask continue
keep = input('Do you want srart to calculate(y/n) :')
if keep=='y':
    # Start calculate
    prc = re.findall(r"\d+", token_prc)
    prc1 = prc[0]
    print(prc1)

    # The last one is print"."

'''

mylist = ["A", "B", "C", "D", "E"]

print("B" in mylist)
>> True

print("G" in mylist)
>> False

'''
