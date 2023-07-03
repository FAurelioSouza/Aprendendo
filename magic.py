import utilits
import pyautogui
import time
import random

#parametros Alch
ALCH_yew_bow = './magicAlch/yew-bow-note.png'
imagem = './magicAlch/skillAlchy.png'
alch1 = './magicAlch/alch1.png'

def status_life():
    print("ok")

def highAlchemy():
    pause = 1
    while pause:
        if utilits.actionColor(imagem, 0.6):
            if utilits.actionColor(alch1, 0.7):
                print("Done")
                time.sleep(0.7)
            elif utilits.actionColor(ALCH_yew_bow, 0.6):
                print("Done")
                time.sleep(0.7)
            else:
                pause = 1
        else:
            print("Não encontrou a magia")
            pyautogui.press('f6')
            time.sleep(0.7)

def afkSplash():
    #print(pyautogui.KEY_NAMES)
    while 1:
        randomKey = utilits.returnKey(random.randint(1,4))
        randomTime = 60*random.randint(2,6) 
        #random.randint(1, 4) 
        print("Tecla que será Apertada: " + randomKey)
        print("Tempo que será feito " + str(randomTime))
        pyautogui.press(randomKey, presses=200)
        time.sleep(randomTime)
