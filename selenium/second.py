# Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# -----  Setup scraping  ----------------------------------------
# Open browser
browser = webdriver.Chrome('./chromedriver')

# Open url
url = "https://postprime.com"
browser.get(url)
sleep(3)
print("Start scraping")

# -----  Login second account  ----------------------------------------
# Start login
testbtn = browser.find_element_by_class_name("Button_button__q6YWL")
testbtn.click()
sleep(2)

startLoginbtn = browser.find_element_by_class_name(
    "LoginDialog_tabContent__nEYko")
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

# --------  Start select up  ------------------------------------------------------

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


# --------  Start get data  ------------------------------------------------------

# Get name
name_datas = browser.find_elements_by_class_name("SymbolDataView_leftSide__lLy3l")
name_values = []
for name_datas in name_datas:
    namevalue = name_datas.text
    name_values.append(namevalue)

print(name_values) # test

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
