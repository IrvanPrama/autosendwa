import pywhatkit
import pyautogui
import time

pywhatkit.sendwhatmsg("+62000000000000", "Test Ppython send wa", 12, 26)
pywhatkit.sendwhatmsg("+62000000000000", "Test Ppython send wa", 12, 27)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')
