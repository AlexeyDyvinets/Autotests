from selenium import webdriver
from auth_data import *
import eel
import time

@eel.expose
def login_dev_ff(org):
        print(org)
        driver = webdriver.Firefox(executable_path='webDrivers\geckodriver.exe')
        driver.get(url=url_dev)
        time.sleep(3)
        orgIDField = driver.find_element_by_id('client_id')
        orgIDField.clear()
        if org == "Internal":
            orgIDField.send_keys(internal_dev_org_id)
            time.sleep(1)
            nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
            time.sleep(1)
            username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
            password_field = driver.find_element_by_id("user_password").send_keys(password)
            login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
        elif org == "Asset Management":
            orgIDField.send_keys(asset_dev_org_id)
            time.sleep(1)
            nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
            time.sleep(1)
            username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
            password_field = driver.find_element_by_id("user_password").send_keys(password)
            login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
        elif org == "CashWerkz":
            orgIDField.send_keys(cashwerkz_dev_org_id)
            time.sleep(1)
            nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
            time.sleep(1)
            username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
            password_field = driver.find_element_by_id("user_password").send_keys(password)
            login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
        else:
            orgIDField.send_keys(fiig_dev_org_id)
            time.sleep(1)
            nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
            time.sleep(1)
            username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
            password_field = driver.find_element_by_id("user_password").send_keys(password)
            login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()

@eel.expose
def login_qa_ff(org):
    print(org)
    driver = webdriver.Firefox(executable_path='webDrivers\geckodriver.exe')
    driver.get(url=url_qa)
    orgIDField = driver.find_element_by_id('client_id')
    orgIDField.clear()
    if org == "Internal":
        orgIDField.send_keys(internal_qa_org_id)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(1)
        username_field = driver.find_element_by_id("user_name").send_keys(regular_userName)
        password_field = driver.find_element_by_id("user_password").send_keys(password)
        login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    elif org == "Asset Management":
        orgIDField.send_keys(asset_qa_org_id)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(1)
        username_field = driver.find_element_by_id("user_name").send_keys(regular_userName)
        password_field = driver.find_element_by_id("user_password").send_keys(password)
        login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    elif org == "CashWerkz":
        orgIDField.send_keys(cashwerkz_qa_org_id)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(1)
        username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
        password_field = driver.find_element_by_id("user_password").send_keys(password)
        login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    else:
        orgIDField.send_keys(fiig_qa_org_id)
        time.sleep(1)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(10)
        username_field = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[3]/td/input").send_keys(fiig_qa_userName)
        password_field = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td/input").send_keys(fiig_password)
        login_button = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td/input").click()

@eel.expose
def login_prod_ff(org):
    print(org)
    if org == "Asset Management":
        driver = webdriver.Firefox(executable_path='webDrivers\geckodriver.exe')
        driver.get(url=url_prod)
        orgIDField = driver.find_element_by_id('client_id')
        orgIDField.clear()
        orgIDField.send_keys(asset_prod_org_id)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(1)
        username_field = driver.find_element_by_id("user_name").send_keys(admin_userName)
        password_field = driver.find_element_by_id("user_password").send_keys(password)
        login_button = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[5]/input").click()
    else:
        driver = webdriver.Firefox(executable_path='webDrivers\geckodriver.exe')
        driver.get(url=url_fiig_prod)
        orgIDField = driver.find_element_by_id('client_id')
        orgIDField.clear()
        orgIDField.send_keys(fiig_prod_org_id)
        time.sleep(1)
        nextButton = driver.find_element_by_xpath('/html/body/app-root/org-field/div/div/div/div/div[2]/input[2]').click()
        time.sleep(10)
        username_field = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[3]/td/input").send_keys(fiig_qa_userName)
        password_field = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[4]/td/input").send_keys(fiig_password)
        login_button = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td/input").click()
