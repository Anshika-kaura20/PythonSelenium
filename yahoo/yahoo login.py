from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
import validators
import os

PROXY_HOST = '107.150.71.43'
PROXY_PORT = '12345'
PROXY_USER = '555'
PROXY_PASS = '555'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""
background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

print(validIP(PROXY_HOST))

valid=validators.url('https://www.yahoo.com/')
if valid==True:
    service=Service("C:\\browserdriver\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    username = os.getlogin()
    chrome_driver = r"C:\Users\{username}\Desktop\selen\chromedriver.exe".format(username=username)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(service=service,options=options)

    print("Url is valid")
else:
    print("Invalid url")
    exit()

driver.get("https://www.yahoo.com/")
driver.find_element_by_xpath('//*[@id="ysignin"]/div').click()
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('anshikakaura20@gmail.com')
driver.find_element_by_xpath('//*[@id="login-signin"]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('ansh20122000')
driver.find_element_by_xpath('//*[@id="login-signin"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ymail"]/div').click()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[7]/div/a/span[1]').click()
time.sleep(3)

try:
    driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div[1]/div/div[1]/div/div/ul/li[1]/span/button/span').click()
except:
    print("failed")

try:
    driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div[1]/div/div[2]/div/div[1]/button/span').click()
except:
    print("no files found")
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[1]/div/a/span[1]').click()
driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div[1]/div/div[1]/div/div/ul/li[2]/div/span/button/span').click()
un_read=driver.find_element_by_xpath('//*[@id="app"]/div[7]/div/div[1]/div/ul/li[4]/button').click()
driver.find_element_by_xpath('//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]').click()
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]').clear()
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]').send_keys("is:unread in:inbox")
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="mail-search"]/div/div/div[1]/ul/li/div/div/input[1]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div/div[1]/ul/li[3]/a/div').click()
time.sleep(2)
star=driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div[2]/div[4]/ul/li[1]/div/header/div[5]/button/span').click()
time.sleep(2)
archive=driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div[1]/div[2]/ul/li[1]/div/button').click()
time.sleep(2)
