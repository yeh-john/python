from selenium import webdriver
from time import sleep


# -----  Start login  ----------------------------------------
# Open browser
browser = webdriver.Chrome('chromedriver')

# Open url
url = "https://postprime.com"
browser.get(url)
sleep(3)
print("start find")

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


# --------  Start get data  ------------------------------------------------------

# Move to chart section
browser.get("https://postprime.com/chart")
sleep(4)

# Start get btc data
# data = browser.find_element_by_class_name("SymbolDataView_vote__kFeaM")

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

print(up_values) # test 

# --------  Logout account  ------------------------------------------------------

logouturl = "https://postprime.com/account?tab=others"
browser.get(logouturl)
sleep(10)

# Click other setting
otherSetting = browser.find_elements_by_class_name("OtherSettings_item__wS_2c")
otherSetting[0].click()
sleep(2)

browser.find_elements_by_class_name("OtherSettings_groupArrow__VrGlE")[2].click()
sleep(6)


test = browser.find_elements_by_xpath('//*[@id="react-tabs-11"]/div/div/div[3]/div[4]')
print(test)


test[0].click()

# logoutbtn = browser.find_element_by_class_name("OtherSettings_subItem__No9zI")




# Video(18:11) :  https://www.youtube.com/watch?v=kvj3On1k66A&list=RDCMUC0xRMqPOyRNPTaL6BxhbCnQ&index=3




# Quit browserotherSetting[2].click()
# browser.quit()
