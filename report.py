#import needed modules
import requests, time, json, sys
from datetime import date

#loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()

#request to API
headers = {
    'cookie': chaves['sz_cookies'],
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
page = requests.get(f'{variaveis["url"]}/monitoring/filter', headers=headers)

#json from API response
lista = page.json()

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

#creates the message string
mensagem = open('model.txt', 'r', encoding='utf8').read()
mensagem = mensagem.replace('{day}', str(hoje.day).zfill(2))
mensagem = mensagem.replace('{month}', str(hoje.month).zfill(2))
mensagem = mensagem.replace('{month_name}', mes(hoje.month))
mensagem = mensagem.replace('{time}', str(hora))
mensagem = mensagem.replace('{waiting}', str(len(lista['sessions']['wait'])))
mensagem = mensagem.replace('{attendance}', str(len(lista['sessions']['attendance'])))
mensagem = mensagem.replace('{navigating}', str(len(lista['sessions']['navigating'])))

#dumps the message into the variables json
variaveis['report'] = mensagem
with open('variables.json', 'w', encoding='utf8') as write_file:
    json.dump(variaveis, write_file)

teste = page.headers['set-cookie'].split(' ')
chaves['sz_cookies'] = teste[0] + " " + teste[10]
with open('keys.json', 'w', encoding='utf8') as write_file:
    json.dump(chaves, write_file)
