from selenium import webdriver
'''
Working firefox webdriver
Using google due to task performed
browser = webdriver.Firefox(executable_path="./geckodriver.exe")
'''
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
# browser.get("https://www.google.com/") # tested/validated for chrome version (80.0). If Chrome updates, download matching version chrome driver. Get version from Chrome>help>about
browser.get('https://lhric.service-now.com/ess/?id=login')

userElem = browser.find_element_by_id('user_name')
userElem.send_keys('kjeffreys')

passwordElem = browser.find_element_by_id('user_password')
passwordElem.send_keys('Jflwin100!')

passwordElem.submit()
