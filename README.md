# mfa-bypass
Python3 script to bypass MFA through phishing


Right click save as on web page in firefox, host in apache

run selenium locally to make sure getting right variables and names

examples
>>> driver = webdriver.Chrome()
>>> driver.get('https://path/to/login')
>>> driver.find_element_by_id('pf.username').send_keys('test')
>>> driver.execute_script("javascript:postOk()")

