import pyautogui
import time
import keyboard
import random

imagem = './highalchy.png'
axe = './axe.png'
dagger = './runedagger.png'
scimitar = './steelscimitar.png'

def highAlchemy():
    while 1:
        if pyautogui.locateOnScreen(imagem, confidence=0.5):
            print("Encontrou a magia")
            valor = pyautogui.locateOnScreen(imagem, confidence=0.5)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            print(valor)
            print(valorCenter)
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            time.sleep(0.7)
            pyautogui.click()
            time.sleep(0.7)
            valor = pyautogui.locateOnScreen(axe, confidence=0.5)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            time.sleep(0.7)
            pyautogui.click()
            time.sleep(0.7)
        else:
            print("Não encontrou a magia")
            pyautogui.press('f4')
            time.sleep(0.7)

def afkSplash():
    #print(pyautogui.KEY_NAMES)
    while 1:
        randomKey = returnKey(random.randint(1,4))
        randomTime = 60*random.randint(2,6) 
        #random.randint(1, 4) 
        print("Tecla que será Apertada: " + randomKey)
        print("Tempo que será feito " + str(randomTime))
        pyautogui.press(randomKey, presses=200)
        time.sleep(randomTime)

def returnKey(valor):
    match valor:
        case 1:
            return 'up'
        case 2:
            return 'down'
        case 3:
            return 'left'
        case 4:
            return 'right'

afkSplash()
