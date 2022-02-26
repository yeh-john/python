# Import
import time
import pyautogui as pgui

# Start define
music = 'https://youtu.be/pFIvWgPjXOw'  # ------ Set music -------
minte = 60

# Ask question
set_time = input("How many minte do you want to set timer :")
print('Please check the volume')
print('You set timer for '+set_time+'minte later')
print('')

# Start program
keep = input('Do you want to start timer(y/n) :')
if keep=='y':
    print('You succes to set timer 'set_time'mintes later.')
    timer =  int(minte)*int(set_time)
    time.sleep(timer)
    # Play music
    pgui.hotkey('winleft','r')
    time.sleep(1)
    pgui.write(music)
    time.sleep(1)
    pgui.hotkey('enter')
else:
    print('Done')
