'''
python으로 telegram message 보내기
'''

import requests

token = '<token>'
base_url = 'https://api.telegram.org'


# 1. getUpdates 를 통해 chat_id를 가져옴

url = f'{base_url}/bot{token}/getUpdates'
res = requests.get(url)
res_dict = res.json()
print(url)

chat_id = str(res_dict['result'][0]['message']['chat']['id'])
print(chat_id)

# 2. 

msg = "와 자동화 했다~"
param = '?chat_id='+chat_id+'&text='+msg

url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}'
print(url)
requests.get(url)

# '''
# python으로 telegram message 보내기
# '''

# import requests

# token = '<token>'
# base_url = 'https://api.telegram.org/'

# response = requests.get('https://api.telegram.org/bot<token>/getUpdates')
# res_dict = response.json()
# print(res_dict['result'][0]['message']['chat']['id'])

# # 1. getUpdates 를 통해 chat_id를 가져옴
# chat_id = str(res_dict['result'][0]['message']['chat']['id'])

# # 2. 
# method = '/sendMessage'
# msg = "telegram.py에서 보내는 메시지"
# param = '?chat_id='+chat_id+'&text='+msg

# url = base_url + token + method + param
# print(url)
# requests.get(url)