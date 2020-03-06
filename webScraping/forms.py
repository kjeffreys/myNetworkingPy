import pyautogui, time
'''
Fill out forms:

Following comments denote the layout of example
'''

# <label value="Name">
# <input type="text">
# <br>

# <label value="Greatest Fear(s)">
# <input type="text">
# <br>

# <label value="What is source?">
# <input type="text">
# <br>

# <label value="Rate Robocop">
# <input type="Radiobox">
# <br>

# <label value="Additional Comments">
# <input type="textArea">
# <br>

# <input type="Submit">
# <br>

'''
My coords
'''
# Click 1
# Incident > Create New
# x=128, y=608 (on half screen; on laptop)
# To get new coords, use gettingTheMousePosition.py

# Click 2
# Field: "Caller"
# x=334, y=453

'''
My impl
'''
# Load the webpage in left Windows snap area on laptop (1366x768)
# visit (manually) url("https://lhric.service-now.com/nav_to.do?uri=%2Fincident.do%3Fsys_id%3D-1%26sysparm_query%3Dactive%3Dtrue%26sysparm_stack%3Dincident_list.do%3Fsysparm_query%3Dactive%3Dtrue")
# Or simply go to lhric service desk and login. 
# !!!Have the navigator expanded!!!

# Form data:
formData = [{"Caller": "Maritza Mendoza", 'School': 'Fleetwood Elementary School', 'Room': '160','Request Type': 'Interactive Displays', 'Category': 'Inquiry / Help', 'State': 'Resolved', 'Assignment group': 'East Ramapo Central School District', 'Assigned to': 'Kyle Jeffreys', 'Description': 'Having issues with Promethean after Windows 10 update',
'Close code': 'Solved Remotely (Permanently)', 'Close notes (Customer Visible)': 'Installed/Updated ActivDriver, ActivInspire, system drivers, BIOS updates.'}]

# TODO: Give the user a chance to kill the script.
for ticketObj in formData:
    print('>>>5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    
    # TODO: Wait until the form page has loaded.
    #not used

    # TODO: Fill out the Name Field.
    '''Extended explanation:
    Field is "Caller" with input for first and last name
    But upon clicking INCIDENT -> Create New,
    This field will automatically gain focus.
    So this will click Create New, enter name, then tab to next field
    where data is needed.
    Original code to click Caller when not using Create new is below
    and commented out for reference.
    '''
    #print('Entering %s info...' % (ticketObj['Caller']))
    #click "Create New"
    #pyautogui.click(82,383)
    #time.sleep(3)
    #pyautogui.click(458,314)
    
    print('Entering %s info...' % (ticketObj['Caller']))
    #pyautogui.write(['\t', '\t'])
    # Enter needs b/c fields aren't text #
    # They look like input="text" #
    # It's more like an AJAX search field though"
    # For text and tab, it considers this an error non-entry"
    pyautogui.click(119,398)
    time.sleep(4)
    pyautogui.click(467, 434)
    pyautogui.write(ticketObj['Caller'])
    pyautogui.press('enter')
    pyautogui.write('\t'*4)
    pyautogui.press('enter')
    pyautogui.write('\t')




    '''
    pyautogui.write(ticketObj['Caller'] + ('\t'*4))
    #pyautogui.write('\t'*4)
    #pyautogui.write(ticketObj['Assignment group'] + '\t')

# TODO: Tab completion not working, enter manually
    #Note: Assignment Group = District
    '''
    
    #pyautogui.write(ticketObj['Assignment group'])

# TODO: Fill out School
    pyautogui.write(ticketObj['School'] + '\t')
    pyautogui.press('enter')
# TODO: Fill out Room # (not query, no enter needed)
    pyautogui.write(ticketObj['Room'] + '\t')
    
# TODO: Fill out Request Type
    pyautogui.write(ticketObj['Request Type'] + '\t')
    pyautogui.press('enter')

# TODO: Fill out Category
    pyautogui.write(ticketObj['Category'] + '\t')
    pyautogui.press('enter')
    pyautogui.write('\t'*4)
# TODO: Fill out "State"
    if(ticketObj['State'] == 'Resolved'):
        for i in range(7):
            pyautogui.press('down')
    print('No tabs')
    pyautogui.write('\t')
    print('One tab')
    time.sleep(10)
    pyautogui.write('\t')
    print('Two tabs')
    time.sleep(10)
    pyautogui.write('\t')
    print('Three tabs')
    time.sleep(10)
    pyautogui.write('\t')
    print('Four tabs')
    time.sleep(20)


    pyautogui.write('\t'*4)
# TODO: Fill out Assignment group
    pyautogui.write(ticketObj['Assignment group'] + '\t')
# TODO: Fill out Assigned to
    pyautogui.write(ticketObj['Assigned to'])
    pyautogui.press('enter')
    pyautogui.write('\t')
    pyautogui.write('\t')
#For some reason the Assignment group WILL tab assign
# So it was skipping the Assigned to field.
    
# TODO: Fill out Description
    pyautogui.write(ticketObj['Description'] + ('\t'*2))
    
# TODO: Close notes
    pyautogui.press('down')
    for i in range(4):
        pyautogui.press('tab')
    pyautogui.write(ticketObj['Close notes (Customer Visible)'])
'''
# Close code
    pyautogui.write(ticketObj['Close code'] + ('\t'*4))
# Close notes
    pyautogui.write(ticketObj['Close notes (Customer Visible'] + '\t')

# submit with pyautogui.press('enter) while Submit button has focus
'''
