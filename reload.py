# import needed modules
import requests
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.headless = True

driver = webdriver.Chrome(service=Service(
    executable_path="/home/ernesto/Github/TelegramReports/modules/SZReports/chromedriver"), options=chrome_options)

driver.get('https://online.sz.chat/')
driver.implicitly_wait(45)
login = driver.find_element(by=By.NAME, value='email')
login.send_keys('ernesto.muniz@online.net.br')
password = driver.find_element(by=By.NAME, value='password')
password.send_keys('9AZaicTk3RKrM74rH83a')
password.submit()
totais = driver.find_element(By.CLASS_NAME, 'qtd')

res = f"sz_user_session={driver.get_cookie('szchat_session')['value']}"

driver.quit

# dump results and send answer
with open('keys.json', 'w') as write_file:
    chaves['sz_cookies'] = res
    json.dump(chaves, write_file)

with open('variables.json', 'w') as write_file:
    variaveis['report'] = 'Session Reloaded!'
    json.dump(variaveis, write_file)
    sys.exit()