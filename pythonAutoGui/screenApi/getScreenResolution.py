import pyautogui

#Obtain the screen size
wh = pyautogui.size()

print(wh)

print(wh[0])

print(wh.width)

print(wh.height)

print(wh[1])

for a in dir(wh):
    if not a.startswith('__'):
        print(a)