
# This program is to go Coinmarketcap to take screenshot in kali linux


# Import tools
import pyautogui as pgui
import datetime
import time


# Start program

# Set today time
now = datetime.datetime.now()
today = now.strftime('%Y/%m/%d')

# Go to btc chart
pgui.hotkey('winleft','r')
time.sleep(2)
pgui.write('https://www.tradingview.com/chart/?symbol=BITSTAMP%3ABTCUSD')
pgui.hotkey('enter')

# Take screenshot
time.sleep(5)
name = 'BTCchart-'+today
pgui.screenshot(name'.png')
