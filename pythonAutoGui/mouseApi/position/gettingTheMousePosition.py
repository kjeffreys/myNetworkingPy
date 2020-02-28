import pyautogui

pyautogui.position() # Get current mouse position

pyautogui.position() # Get position again

p = pyautogui.position() # And again

print(p)

print(p[0])

print(p.x)