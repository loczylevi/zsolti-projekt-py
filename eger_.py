import pyautogui
import time
time.sleep(5)

pyautogui.moveTo(400, 300, 5)  #mozgasd az egeret x,y kordináta harmadik érték hány másodper alatt
pyautogui.moveRel(600, 700, 7) 
pyautogui.dragTo(500, 600, 5) # mozgasd az egeret DE közben nyomd hosszan a bal clikket
pyautogui.dragRel(800, 1200, 8)

pyautogui.click(70, 178)

pyautogui.scroll(8, 300, 400)
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY) # görgetés
