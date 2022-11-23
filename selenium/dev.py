# Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from datetime import date
import math


# -----  Setup scraping  ----------------------------------------
# Open browser

# Mac version
browser = webdriver.Chrome()

"""
# Linux version
browser = webdriver.Chrome("./chromewebdriver")
"""

# Open url
url = "https://postprime.com"
browser.get(url)
sleep(3)
print("Start scraping")


# -----  Login first account  ----------------------------------------
# Start login
testbtn = browser.find_element_by_class_name("Button_button__q6YWL")
testbtn.click()
sleep(2)

startLoginbtn = browser.find_element_by_class_name("LoginDialog_tabContent__nEYko")
startLoginbtn.click()
sleep(2)

# Type mail
mailInput = browser.find_element_by_id("email-login-email")
mailInput.send_keys('enipjlu144@iemail.one')
sleep(2)

# Click login btn
preLoginbtn = browser.find_element_by_class_name("LoginDialog_normal__VHlec")
preLoginbtn.click()
sleep(4)

# Type passwd
pwdInput = browser.find_element_by_id("email-login-password")
pwdInput.send_keys('Go121212')
sleep(2)

# Start login
loginbtn = browser.find_element_by_class_name("LoginDialog_normal__VHlec")
loginbtn.click()
sleep(2)


# --------  Start vote up  ------------------------------------------------------

# Move to chart section
browser.get("https://postprime.com/chart")
sleep(4)


# Sp500 vote up
voteUpbtn_sp500 = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div')
try:
  voteUpbtn_sp500.click()
except:
  print("Already voted sp500 up")
sleep(1)


# Move to bottom
background = browser.find_element_by_css_selector("body")

for i in range(5):
    background.send_keys(Keys.SPACE)
    sleep(1)


# Btc vote up
voteUpbtn_btc = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div')
try:
  voteUpbtn_btc.click()
except:
  print("Already voted btc up")
sleep(1)


# Nasdap100
voteUpbtn_ndq = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div')
try:
  voteUpbtn_ndq.click()
except:
  print("Already voted ndq up")
sleep(1)


# --------  Start get up data  ------------------------------------------------------

# Get name
name_datas = browser.find_elements_by_class_name("SymbolDataView_leftSide__lLy3l")
name_values = []
for name_datas in name_datas:
    namevalue = name_datas.text
    name_values.append(namevalue)

print(name_values) # test


# Get up values
up_datas = browser.find_elements_by_class_name("SymbolDataView_vote__kFeaM")

up_values = []
for up_datas in up_datas:
    upvalue = up_datas.text
    up_values.append(upvalue)

# Delete value
del up_values[1]
del up_values[2]
del up_values[3]

print(up_values) # test 
sleep(2)

# --------  Logout first account  ------------------------------------------------------

logouturl = "https://postprime.com/account?tab=others"
browser.get(logouturl)
sleep(5)

# Click other setting
otherSetting = browser.find_elements_by_class_name("OtherSettings_item__wS_2c")
otherSetting[0].click()
sleep(2)

browser.find_elements_by_class_name("OtherSettings_groupArrow__VrGlE")[2].click()
sleep(6)


logoutBtn = browser.find_elements_by_xpath('//*[@id="react-tabs-11"]/div/div/div[3]/div[4]')
logoutBtn[0].click()
sleep(5)


# -----  Login second account  ----------------------------------------
# Start login
testbtn = browser.find_element_by_class_name("Button_button__q6YWL")
testbtn.click()
sleep(2)

startLoginbtn = browser.find_element_by_class_name("LoginDialog_tabContent__nEYko")
startLoginbtn.click()
sleep(2)

# Type mail
mailInput = browser.find_element_by_id("email-login-email")
mailInput.send_keys('parpoxc374@couldmail.com')
sleep(2)

# Click login btn
preLoginbtn = browser.find_element_by_class_name("LoginDialog_normal__VHlec")
preLoginbtn.click()
sleep(4)

# Type passwd
pwdInput = browser.find_element_by_id("email-login-password")
pwdInput.send_keys('Go121212')
sleep(2)

# Start login
loginbtn = browser.find_element_by_class_name("LoginDialog_normal__VHlec")
loginbtn.click()
sleep(2)


# --------  Start vote down  ------------------------------------------------------

# Move to chart section
browser.get("https://postprime.com/chart")
sleep(4)

# Sp500 vote down
voteDownbtn_sp500 = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div')
try:
  voteDownbtn_sp500.click()
except:
  print("Already voted sp500 down")
sleep(1)


# Move to bottom
background = browser.find_element_by_css_selector("body")
for i in range(5):
    background.send_keys(Keys.SPACE)
    sleep(1)


# Btc vote down
voteDownbtn_btc = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div')
try:
  voteDownbtn_btc.click()
except:
  print("Already voted btc down")
sleep(1)


# Nasdap100 vote down
voteDownbtn_ndq = browser.find_element_by_xpath('//*[@id="react-tabs-9"]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div')
try:
  voteDownbtn_ndq.click()
except:
  print("Already voted ndq down")
sleep(1)


# --------  Start get down data  ------------------------------------------------------

# Get down values
down_datas = browser.find_elements_by_class_name("SymbolDataView_vote__kFeaM")

down_values = []
for down_datas in down_datas:
    downvalue = down_datas.text
    down_values.append(downvalue)

# Delete value
del down_values[0]
del down_values[1]
del down_values[2]

print(down_values) # test 
sleep(1)

browser.close()
sleep(3)


# -------- Calculate datas  ------------------------------------------------------

# Total vote amount
total_values = [int(x)+int(y) for (x,y) in zip(up_values, down_values)]

# Up percentage
up_per = [int(x)/int(y) for (x,y) in zip(up_values, total_values)]
up_per = [i * 100 for i in up_per]
up_per = [math.floor(i) for i in up_per]
up_per = [str(i)+"%" for i in up_per]

# Down percentage
down_per = [int(x)/int(y) for (x,y) in zip(down_values, total_values)]
down_per = [i * 100 for i in down_per]
down_per = [math.floor(i) for i in down_per]
down_per = [str(i)+"%" for i in down_per]

sleep(3)


# -------- Export datas  ------------------------------------------------------
df = pd.DataFrame()
df['Name'] = name_values
df['Vote up amount'] = up_values
df['Vote down amount'] = down_values
df['Total vote amount'] = total_values
df['Up percentage'] = up_per
df['Down percentage'] = down_per
sleep(2)

# Set date
today = date.today()

filename = "result"+str(today)+".csv"

df.to_csv(filename, index=False)
