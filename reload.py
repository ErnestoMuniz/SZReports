#import needed modules
import requests, json, sys

#loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()

#Login
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'content-type': 'application/json',
    'referer': f'{variaveis["url"]}static/signin',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"operationName":"login","variables":{"email":"' + chaves["user"] + '","password":"' + chaves["password"] + '","language":"pt-BR"},"query":"mutation login($email: String\\u0021, $password: String\\u0021, $language: String\\u0021) { login(email: $email, password: $password, language: $language) { token intend client_id user { name _id email type __typename } __typename }}"}'

response = requests.post('https://online.sz.chat/graphql', headers=headers, data=data)

cookie = response.headers['Set-Cookie'].split(';')[0]

#Request authorization cookies
headers = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': f'{variaveis["url"]}static/signin',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': cookie,
}

response = requests.get('https://online.sz.chat/dashboard', headers=headers)

res = response.headers['Set-Cookie'].split(';')
res = f'{res[0]};{res[6].split(",")[1]};'

#dump results and send answer
with open('keys.json', 'w') as write_file:
    chaves['sz_cookies'] = res
    json.dump(chaves, write_file)

with open('variables.json', 'w') as write_file:
    variaveis['report'] = 'Session Reloaded!'
    json.dump(variaveis, write_file)
    sys.exit()
