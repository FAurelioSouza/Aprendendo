import pyautogui
import time

#parametros gerais
BUTTOM_CLOSE = './botaoGeral/close.png'
BUTTOM_ALL = './botaoGeral/put-all.png'


def actionColor():
    color = (255, 0, 0)
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pyautogui.moveTo(x + 10, y, 0.3, logScreenshot=False)
                pyautogui.click()
                return
                
def actionMouse(item, considerar):
    if pyautogui.locateOnScreen(item, confidence=considerar):
        valor = pyautogui.locateOnScreen(item, confidence=considerar)
        valorCenter = pyautogui.center((valor[0], valor[1],valor[2], valor[3]))
        pyautogui.moveTo(valorCenter[0], valorCenter[1], 0.3, logScreenshot=False)
        pyautogui.click()
        
        return True
    else:
        return False

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