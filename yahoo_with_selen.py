# import undetected_chromedriver.v2 as uc
# import time


# PROXY = "23.229.125.109:9138"

		
# email = 'pauybeto26@gmail.com'
# password = '$sXNc-qqnQ8BHNyf'
# recovery_email = 'marlene131978quinn@hotmail.com'


# options = uc.ChromeOptions()


# options.add_argument('--proxy-server=%s' % PROXY)
# options.add_argument("user-data-dir=C:/Users/{username}/Desktop/selen/{x}".format(x='akd', username='Administrator'))


# def login(web_driver):
#     driver.get("https://www.yahoo.com/")
#     driver.find_element_by_id("identifierId").send_keys(email)
#     time.sleep(5)
#     driver.find_elements_by_tag_name("button")[2].click()
#     time.sleep(5)
#     driver.find_element_by_name("password").send_keys(password)
#     time.sleep(5)
#     driver.find_elements_by_tag_name("button")[1].click()
#     time.sleep(5)

# def confirm_recovery(web_driver):
#     driver.find_element_by_xpath("//div[contains(text(), 'Confirm your recovery email')]").click()
#     time.sleep(5)
#     driver.find_element_by_id("knowledge-preregistered-email-response").send_keys(recovery_email)
#     time.sleep(5)
#     driver.find_elements_by_tag_name("button")[0].click()
#     time.sleep(5)
    


# driver = uc.Chrome(options=options)
# with driver:
#     login(driver)
#     print(driver.title)
#     if 'Inbox' not in driver.title:
#         confirm_recovery(driver)
    
#     input('continue..')
    
# exit(0)

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
import validators
import zipfile
import os
import custom_logger

logger = custom_logger.get_logger(__name__)

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

# valid=validators.url('https://www.yahoo.com/')
# if valid==True:
#     service=Service("C:\\browserdriver\\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     username = os.getlogin()
#     chrome_driver = r"C:\Users\{username}\Desktop\selen\chromedriver.exe".format(username=username)
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     options.add_experimental_option('useAutomationExtension', False)
#     driver=webdriver.Chrome(service=service,options=options)

#     print("Url is valid")
# else:
#     print("Invalid url")
#     exit()

def open_mail():
    driver.find_element_by_xpath('//*[@id="ymail"]/div').click()
    time.sleep(3)

def open_spam():
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[7]/div/a/span[1]').click()  #open spam
    time.sleep(3)
    print("opened spam mails")
    try:
        driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div[1]/div/div[1]/div/div/ul/li[1]/span/button/span').click()  #select all spam mails
        driver.find_elements_by_xpath('//*[@id="mail-app-component"]/div/div/div[1]/div/div[2]/div/div[4]/button/span').click()       #click on not spam button
        print("spam mails restore to inbox")
    except:
        print("Your Spam folder is empty")
    time.sleep(3)

def open_inbox(count):       
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[3]/ul/li[1]/div/a/span[1]').click()    #click inbox
    time.sleep(2)                    
    # un_read=driver.find_element_by_xpath('//*[@id="app"]/div[7]/div/div[1]/div/ul/li[4]/button').click()  #click on unread emails
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
    for i in range(1,count+1):
        star()
        archive_btn()
        go_back()


def star():
    time.sleep(6)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/header/div[3]/div[2]/button/span').click()
    time.sleep(2)

def archive_btn():
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/ul/li[1]/div/button/span').click()
    time.sleep(2)

def go_back():
    driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/button').click()
    time.sleep(3)


print("Script Started...")

start = int(input("Start profile: "))
end = int(input("End profile: "))

for x in range(start, end):
    print(f"Running profile: {x} from range({start}-{end})")
    username = os.getlogin()
    options = webdriver.ChromeOptions()
    service=Service("C:\\browserdriver\\chromedriver.exe")
        # pluginfile = 'proxy_auth_plugin.zip'
        # with zipfile.ZipFile(pluginfile, 'w') as zp:
        #     zp.writestr("manifest.json", manifest_json)
        #     zp.writestr("background.js", background_js)
        # options.add_extension(pluginfile)
       
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:/Users/{username}/Desktop/selen/{x}".format(x=x, username=username))

    driver = None
    try:
        driver = webdriver.Chrome(service=service,options=options)
        driver.set_window_size(1200, 1000)
        print(driver.get_window_size())
        time.sleep(3)
        driver.get("https://www.yahoo.com/")
        open_mail()
        # open_spam()
        open_inbox(5)
        

    except Exception as e:
        if driver:
            driver.quit()
            print(e)
            logger.error(f"Error Running profile: {x} from range({start}-{end})")
            continue

    print("\t{x}: Finished...".format(x=x))
    driver.quit()

print("Script Finished...")




