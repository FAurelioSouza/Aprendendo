import pyautogui
import time
import fletching

cannon = './reload.png'
safespot = './safespot.png'

def cannonAFK():
    while 1:
        print("loop")
        if pyautogui.locateOnScreen(cannon, confidence=0.5):
            print("Reload Cannon")
            valor = pyautogui.locateOnScreen(cannon, confidence=0.5)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            print(valor)
            print(valorCenter)
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.4, logScreenshot=False)
            time.sleep(0.7)
            pyautogui.click()
            time.sleep(2)

            valor = pyautogui.locateOnScreen(safespot, confidence=0.9)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            time.sleep(0.7)
            pyautogui.click()
            time.sleep(0.7)

def main():
    fletching.fletchingBowU()

if __name__ == '__main__':
    main()