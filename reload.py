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

data = "{\n\t\"query\": \"mutation {\\n  login(\\n    email: \\\"" + chaves['user'] + "\\\"\\n    password: \\\"" + chaves['password'] + "\\\"\\n    language: \\\"pt-BR\\\"\\n    recaptchaV3Token: \\\"\\\"\\n    recaptchaV2Token: \\\"\\\"\\n  ) {\\n    token\\n  }\\n}\\n\"\n}"

response = requests.post('https://online.sz.chat/graphql', headers=headers, data=data)

res = f"sz_user_session={response.json()['data']['login']['token']}"

#dump results and send answer
with open('keys.json', 'w') as write_file:
    chaves['sz_cookies'] = res
    json.dump(chaves, write_file)

with open('variables.json', 'w') as write_file:
    variaveis['report'] = 'Session Reloaded!'
    json.dump(variaveis, write_file)
    sys.exit()
