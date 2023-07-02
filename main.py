import pyautogui
import time
import keyboard
import random

#imagem = './alchy.png'
imagem = './skillAlchy.png'
axe = './axe.png'
dagger = './runedagger.png'
scimitar = './steelscimitar.png'
cannon = './reload.png'
safespot = './safespot.png'

alch1 = './alch1.png'
alch2 = './alch2.png'
alch3 = './alch3.png'

arrow = './arrowsM.png'
pena = './pena.png'

logNote = './log.png'
log = './logg.png'
bank = './bank.png'
knif = './knif.png'

def highAlchemy():
    pause = 1
    while pause:
        if pyautogui.locateOnScreen(imagem, confidence=0.6):
            print("Encontrou a magia")
            valor = pyautogui.locateOnScreen(imagem, confidence=0.6)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            print(valor)
            print(valorCenter)
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            pyautogui.click()

            if pyautogui.locateOnScreen(alch1, confidence=0.5):
                valor = pyautogui.locateOnScreen(alch1, confidence=0.5)
                valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                pyautogui.click()
                time.sleep(0.7)
            elif pyautogui.locateOnScreen(alch2, confidence=0.5):
                valor = pyautogui.locateOnScreen(alch2, confidence=0.5)
                valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                pyautogui.click()
                time.sleep(0.7)
            else:
                pause = 0
        else:
            print("Não encontrou a magia")
            pyautogui.press('f6')
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

def fletchingFeather():
    pause = 1
    while pause:
        if pyautogui.locateOnScreen(arrow, confidence=0.7):
            print("Encontrou a magia")
            valor = pyautogui.locateOnScreen(arrow, confidence=0.7)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            print(valor)
            print(valorCenter)
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            pyautogui.click()

            if pyautogui.locateOnScreen(pena, confidence=0.8):
                valor = pyautogui.locateOnScreen(pena, confidence=0.8)
                valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                pyautogui.click()
                time.sleep(0.7)
                pyautogui.press('space')
                time.sleep(10.5)
            else:
                pause = 0
        else:
            print("Não encontrou os items")
            pause = 0
            time.sleep(0.7)

def fletchingLOG():
    pause = 1
    while pause:
        if pyautogui.locateOnScreen(logNote, confidence=0.8):
            print("Encontrou a magia")
            valor = pyautogui.locateOnScreen(logNote, confidence=0.8)
            valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
            print(valor)
            print(valorCenter)
            pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
            pyautogui.click()

            if pyautogui.locateOnScreen(bank, confidence=0.5):
                valor = pyautogui.locateOnScreen(bank, confidence=0.5)
                valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                pyautogui.click()
                time.sleep(0.9)
                pyautogui.press('1')
                time.sleep(0.7)
                if pyautogui.locateOnScreen(knif, confidence=0.6):
                    valor = pyautogui.locateOnScreen(knif, confidence=0.6)
                    valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                    pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                    pyautogui.click()
                    time.sleep(0.7)
                    if pyautogui.locateOnScreen(log, confidence=0.8):
                        valor = pyautogui.locateOnScreen(log, confidence=0.8)
                        valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
                        print(valor)
                        print(valorCenter)
                        pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
                        pyautogui.click()
                        time.sleep(0.9)
                        pyautogui.press('space')
                        time.sleep(30)

            else:
                pause = 0
        else:
            print("Não encontrou os items")
            pause = 0
            time.sleep(0.7)

fletchingFeather()
