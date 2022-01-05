from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auth_data import *
import eel
import time

eel.init("GUI")

@eel.expose
def dev_int_log():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    global driver
    driver = webdriver.Chrome(chrome_options = options, executable_path='chromeDriver\chromedriver.exe')
    driver.get(url=url)
    orgIDField = driver.find_element_by_id('client_id')
    orgIDField.clear()
    orgIDField.send_keys(internal_dev_org_id)
    time.sleep(2)
    nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
    time.sleep(2)
    username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
    password_field = driver.find_element_by_id("user_password").send_keys(password)
    login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    time.sleep(10)

@eel.expose
def dev_ass_log():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    global driver
    driver = webdriver.Chrome(chrome_options = options, executable_path='chromeDriver\chromedriver.exe')
    driver.get(url=url)
    orgIDField = driver.find_element_by_id('client_id')
    orgIDField.clear()
    orgIDField.send_keys(asset_dev_org_id)
    time.sleep(2)
    nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
    time.sleep(2)
    username_field = driver.find_element_by_id("user_name").send_keys(regular_userName)
    password_field = driver.find_element_by_id("user_password").send_keys(password)
    login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    time.sleep(10)

@eel.expose
def dev_cash_log():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    global driver
    driver = webdriver.Chrome(chrome_options = options, executable_path='chromeDriver\chromedriver.exe')
    driver.get(url=url)
    orgIDField = driver.find_element_by_id('client_id')
    orgIDField.clear()
    orgIDField.send_keys(cashwerkz_dev_org_id)
    time.sleep(2)
    nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
    time.sleep(2)
    username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
    password_field = driver.find_element_by_id("user_password").send_keys(password)
    login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    time.sleep(10)

@eel.expose
def dev_fiig_log():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    global driver
    driver = webdriver.Chrome(chrome_options = options, executable_path='chromeDriver\chromedriver.exe')
    driver.get(url=url)
    orgIDField = driver.find_element_by_id('client_id')
    orgIDField.clear()
    orgIDField.send_keys(fiig_dev_org_id)
    time.sleep(2)
    nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
    time.sleep(2)
    username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
    password_field = driver.find_element_by_id("user_password").send_keys(password)
    login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    time.sleep(10)
    
eel.start("main.html")