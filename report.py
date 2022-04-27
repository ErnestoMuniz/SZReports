#import needed modules
import requests, time, json, sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()

# Get campaign id
camp = variaveis['campaigns'][variaveis['arg']]

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.headless = True
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(
    executable_path="./chromedriver"), options=chrome_options)

driver.get(variaveis['url'])
driver.implicitly_wait(45)
login = driver.find_element(by=By.NAME, value='email')
login.send_keys(chaves['user'])
password = driver.find_element(by=By.NAME, value='password')
password.send_keys(chaves['password'])
password.submit()
driver.find_element(By.CLASS_NAME, 'user-image')
driver.get(variaveis['url']+'monitoring/filter')
lista = json.loads(driver.find_element(By.TAG_NAME, 'pre').text)
driver.close()

#creates time and date objects
hoje = date.today()
t = time.localtime()
hora = time.strftime("%H:%M", t)

#converts number to name of months
def mes(arg):
	if arg == 1:
		return "janeiro"
	if arg == 2:
		return "fevereiro"
	if arg == 3:
		return "março"
	if arg == 4:
		return "abril"
	if arg == 5:
		return "maio"
	if arg == 6:
		return "junho"
	if arg == 7:
		return "julho"
	if arg == 8:
		return "agosto"
	if arg == 9:
		return "setembro"
	if arg == 10:
		return "outubro"
	if arg == 11:
		return "novembro"
	if arg == 12:
		return "dezembro"

# Store counts
waiting = 0
attendance = 0

# Loop through each queue
for client in lista['sessions']['wait']:
	if client['campaign_id'] == camp:
		waiting += 1

for client in lista['sessions']['attendance']:
	if client['campaign_id'] == camp:
		attendance += 1

#creates the message string
mensagem = open('model.txt', 'r', encoding='utf8').read()
mensagem = mensagem.replace('{day}', str(hoje.day).zfill(2))
mensagem = mensagem.replace('{month}', str(hoje.month).zfill(2))
mensagem = mensagem.replace('{month_name}', mes(hoje.month))
mensagem = mensagem.replace('{time}', str(hora))
mensagem = mensagem.replace('{waiting}', str(waiting))
mensagem = mensagem.replace('{attendance}', str(attendance))
mensagem = mensagem.replace('{navigating}', str(len(lista['sessions']['navigating'])))
mensagem = mensagem.replace('{campaign}', variaveis['arg'].capitalize())

#dumps the message into the variables json
variaveis['report'] = mensagem
with open('variables.json', 'w', encoding='utf8') as write_file:
    json.dump(variaveis, write_file)