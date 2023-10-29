import pyautogui   # a könyvtár be importálása
import time         # a könyvtár be importálása
kepernyo_szelesseg, kepernyo_magassag = pyautogui.size() # megadja mekkora a kepernyo széllesége és magasságát.

print(f"Képernyő szélessege: {kepernyo_szelesseg}")
print(F"Képernyő magassága: {kepernyo_magassag}")

time.sleep(3)   # várj 3 műsodpercet
aktualis_eger_pozi_X, aktualis_eger_pozi_Y = pyautogui.position() # megadja az egér aktuális pozicioját X,Y kordinátában

print(f"Az egered X poziciója: {aktualis_eger_pozi_X}")
print(F"Az egered Y poziciója: {aktualis_eger_pozi_Y}")

pyautogui.moveTo(100, 150) # mennyen az egér x=100 és y=150 pozicióban.

pyautogui.click()          # Clickkelj az egérrel.
pyautogui.click(100, 200)  # gyere ezekbe a kordinátákba és klikkelj oda

pyautogui.move(400, 0)      # gyere ezekbe a kordinátákba egérrel
pyautogui.doubleClick()     # dupla kattintás
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # gyere ide 2 másodperc alatt

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
    pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
