# mfa-bypass
Python3 script to bypass MFA through phishing


Right click save as on web page in firefox, host in apache

run selenium locally to make sure getting right variables and names

examples
python3
driver = webdriver.Chrome()

driver.get('https://path/to/login')

driver.find_element_by_id('pf.username').send_keys('test')

driver.execute_script("javascript:postOk()")


All modified from:

https://github.com/pan0pt1c0n/Yippee-Ki-Yay-MFA-er/blob/master/bypass.py
