import utilits
import pyautogui
import time

#parametros Fletching
FLETCHING_yewlog = './fletching/yew-log.png'
FLETCHING_knif = './fletching/knif.png'
FLETCHING_yew_bow_u = './fletching/yew-bow-u.png'
FLETCHING_yew_bow_u_2 = './fletching/yew-bow-u.png'
FLETCHING_string_bow = './fletching/string-bow.png'

def fletchingBowU():
    pause = 1
    while pause:
        utilits.actionColor()
        time.sleep(1)
        if utilits.actionMouse(FLETCHING_yew_bow_u, 0.6):
            print("Achou: BOW U")
            if utilits.actionMouse(FLETCHING_yewlog, 0.6):
                print("Achou: YEW LOG")
                time.sleep(1)
                if utilits.actionMouse(utilits.BUTTOM_CLOSE, 0.7):
                    print("Achou: BUTTOM CLOSE")
                    time.sleep(1)
                    if utilits.actionMouse(FLETCHING_knif, 0.6):
                        print("Achou: KNIF")
                        if utilits.actionMouse(FLETCHING_yewlog, 0.7):
                            time.sleep(1)
                            print("Achou: YEW LOG")
                            pyautogui.press('3')
                            time.sleep(48)
        else:
            pause = 0                    
   
def fletchingFullbow():
    pause = 1
    while pause:
        utilits.actionColor()
        time.sleep(1)
        if utilits.actionMouse(utilits.BUTTOM_ALL, 0.7):
            print("Achou: BUTTOM ALL")
            time.sleep(1)
            if utilits.actionMouse(FLETCHING_string_bow, 0.7):
                print("Achou: STRING BOW")
                time.sleep(1)
                if utilits.actionMouse(FLETCHING_yew_bow_u_2, 0.3):
                    print("Achou: BOW U 2")
                    time.sleep(1)
                    if utilits.actionMouse(utilits.BUTTOM_CLOSE, 0.7):
                        print("Achou: BUTTOM CLOSE")
                        time.sleep(1)
                        if utilits.actionMouse(FLETCHING_string_bow, 0.7):
                            print("Achou: STRING BOW")
                            time.sleep(1)
                            if utilits.actionMouse(FLETCHING_yew_bow_u, 0.6):
                                time.sleep(1)
                                print("Achou: STRING BOW")
                                pyautogui.press('space')
                                time.sleep(16)
