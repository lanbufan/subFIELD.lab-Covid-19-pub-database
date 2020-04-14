# daily download of LitCovid .ris file to have the most up-to-date list of publications

def dwl_pdf():
    """
    need to log in, which I dont mind doing, but I have not yet managed to get all the steps locked in to log in....in progress
    """
    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        #print ii.tag_name
        len_id = len(ii.get_attribute('id'))
        if len_id == 32:
            if flag_first_dwl == True:
                # needs to log in
                    print(ii.get_attribute('id'))    # id name as string
                    print(len(ii.get_attribute('id')))    # id name as string
                    ii.click()
                    sleep(20)
                    wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[3]/p/a')))
                    driver.find_elements_by_xpath('/html/body/div[3]/p/a')
                    email = 'f.lachapelle@alumni.ubc.ca'
                    pwd = 'Marion#fourcade@20ll'
                    email_box= driver.find_element_by_xpath('//*[@id="login-modal-email-input"]')
                    email_box.send_keys(email)
                    pwd = driver.find_element_by_xpath('//*[@id="login-modal-password-input"]')
                    pwd.send_keys(pwd)
                    driver.find_element_by_xpath('//*[@id="js-for-recaptcha--login-form"]/div[3]/div[2]/input').click()
                    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="js-bootstrap-modal-354"]/div/div/div/div/div/div[3]/span')))
                    ii.click()
                    driver.find_element_by_xpath('//*[@id="js-bootstrap-modal-354"]/div/div/div/div/div/div[3]/span').click()
                    sleep(5)
                    flag_first_dwl = False
            else:
                print(ii.get_attribute('id'))    # id name as string
                print(len(ii.get_attribute('id')))    # id name as string
                ii.click()
                wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="js-bootstrap-modal-354"]/div/div/div/div/div/div[3]/span')))
                driver.find_element_by_xpath('//*[@id="js-bootstrap-modal-354"]/div/div/div/div/div/div[3]/span').click()
                sleep(5)

from pprint import pprint
from random import choice
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import json
import os
import random
import selenium
import shutil
import time
from time import sleep

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('C:\\Users\\cinep\\Desktop\\covid_pub_db\\Data Source\\ACADEMIA\\lit_activity_report.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

rot_ua = [

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        ]

storm_ips = [
            '37.48.118.90:13042',
            '83.149.70.159:13042'
            ]

chrome_options = ChromeOptions()
chrome_ua = "--user-agent=" + choice(rot_ua)
chrome_options.add_argument(chrome_ua)
storm_ip = choice(storm_ips)
print(str(storm_ip))

folder_path = "C:\\Users\\cinep\\Desktop\\covid_pub_db\\Data Source\\ACADEMIA\\daily_dwl\\"

prefs = {"plugins.always_open_pdf_externally": True,
         "download.default_directory":folder_path}

chrome_options.add_experimental_option("prefs",prefs)

chrome_options.add_experimental_option('prefs', prefs)
desired_caps = chrome_options.to_capabilities()
proxy = webdriver.Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = storm_ip
proxy.add_to_capabilities(desired_caps)

driver = webdriver.Chrome("C:/chromedriver.exe", chrome_options=chrome_options, desired_capabilities=desired_caps)

driver.get("https://www.academia.edu/Documents/in/Coronavirus_COVID-19")
wait = WebDriverWait(driver, 10)

l_raw_pub = []
flag_first_page = True
flag_first_dwl = True
for page in range(1, 77):
    pprint('current page {}'.format(str(page)))
    for i in range(1, 21):
        pprint('current pub {}'.format(str(i)))

        if i == 1:
            wait.until(ec.presence_of_element_located((By.XPATH, f'//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[{str(i)}]/div')))
            pub = driver.find_element_by_xpath(f'//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[{str(i)}]/div')
            l_raw_pub.append(pub.text)
        else:
            pub = driver.find_element_by_xpath(f'//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[{str(i)}]/div')
            l_raw_pub.append(pub.text)


    # end of page
    if flag_first_page == True:
        flag_first_page = False
        driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[2]/ul/li/a').click()
    else:
        driver.get(f'https://www.academia.edu/Documents/in/Coronavirus_COVID-19?page={str(page)}')

with open('l_academia_scrape_2020_04_13_p1_p70.json', 'w') as j:
    json.dump(l_raw_pub, j)

