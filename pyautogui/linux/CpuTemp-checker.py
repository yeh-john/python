import time
import pyautogui as pgui


while True:
    # Start copy cpu temp
    time.sleep(1) # 1200 = 2 minutes
    pgui.hotkey('winleft')
    time.sleep(5)
    pgui.write('terminal')
    time.sleep(3)
    pgui.hotkey('enter')
    time.sleep(4)
    pgui.write('sensors | xclip -sel clip')
    time.sleep(4)
    pgui.hotkey('enter')
    time.sleep(5)

    # Open firefox and start upload cpu temp
    time.sleep(5)
    pgui.write("firefox https://nodejs-chatboard.herokuapp.com")
    time.sleep(6)
    pgui.hotkey('enter')
    time.sleep(25)
    pgui.hotkey('tab')
    time.sleep(5)
    pgui.hotkey('ctrl', 'v')
    time.sleep(5)
    pgui.hotkey('enter')
    time.sleep(5)
    pgui.hotkey('ctrl', 'w')
    time.sleep(10)
    pgui.write('exit')
    time.sleep(5)
    pgui.hotkey('enter')
