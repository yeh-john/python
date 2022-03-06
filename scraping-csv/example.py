# This is news scraping system can create csv file

# Start import
import requests as req
from bs4 import BeautifulSoup
from csv import writer

# Setting info
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
url = 'https://decrypt.co/news'

# Start scraping
page = req.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Get news
num = 0
news = soup.find_all('h2')

# Setting CSV file info   'w' is write
with open('news.csv','w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    head_row = ['Number', 'News']
    thewriter.writerow(head_row)

    # define name
    for div in news:
        newss = div.text
        num = num+1
        info = [num, newss]

        # Create CSV file
        thewriter.writerow(info)
