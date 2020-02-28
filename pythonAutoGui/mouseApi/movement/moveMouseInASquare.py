import pyautogui

for i in range(10):
    pyautogui.moveTo(600,200, duration=0.25)
    pyautogui.moveTo(1000,200, duration=0.25)
    pyautogui.moveTo(1000,600, duration=0.25)
    pyautogui.moveTo(600,600, duration=0.25)
    #Note: loop causes the movement back to origin

    '''
    Loop without duration leads to instant TELEPORTATION OF CURSOR!!! :D
    '''
for i in range(10):
    pyautogui.moveTo(600,200)
    pyautogui.moveTo(1000,200)
    pyautogui.moveTo(1000,600)
    pyautogui.moveTo(600,600)