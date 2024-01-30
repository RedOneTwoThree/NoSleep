import pyautogui
import time

pyautogui.FAILSAFE = False

print('Press Ctrl-C to quit.')

width, height = pyautogui.size()

try:
    while True:
        time.sleep(120)
        for i in range(0, 50):
            pyautogui.moveTo(0, i * 5)
        for i in range(0, 3):
            pyautogui.press('shift')
except KeyboardInterrupt:
    print('\n')
