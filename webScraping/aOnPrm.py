import pyautogui, time
# work screen on right side for positioning

print('>>>5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
time.sleep(5)


#Section: Get to computer page:
'''
# pyautogui.position() # Get current mouse position
# Devices position: x=750,y=214
pyautogui.click(750,214)

# Workstations position: x=944,y=366
pyautogui.click(944,366)

# Instruction position: x=976,281
pyautogui.click(976,281)
'''

#Section (upper right snap zcc, lower right snap remote window)

#Click Remote Control...
pyautogui.click(745,311)
time.sleep()

#Click okay to remote
pyautogui.click(1027,311)
time.sleep(5)

# another ok dialog
pyautogui.click(1090,200)
time.sleep(10)

# open Chrome
#pyautogui.doubleClick(782,429,0.1,button='LEFT')
#time.sleep(20)

# Click search bar
pyautogui.click(756,719)
pyautogui.click(856,559)


