# install pyautogui module on your terminal -- pip install PyAutoGUI
# you can sen 3000 times 'I Love You' on your sweetheart for LOL

import pyautogui as py
import time

message = "***spam***"
count = 1
time.sleep(2)

for i in range(100):  
    py.typewrite(message + " " + str(count))
    py.press('Enter')
    count = count + 1

py.typewrite("***spam***")
py.press('Enter')
