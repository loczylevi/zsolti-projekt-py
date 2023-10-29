import pyautogui
import time

while True:
    x,y = pyautogui.position()
    time.sleep(0.5)
    print(f"X:\t{x}\tY:\t{y}")
    c = pyautogui.onScreen(x, y)
    print(c)
    
