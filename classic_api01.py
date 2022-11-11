import requests
import pprint
import time

TOKEN = '716618019:AAFnQ5Qqokl3MX-Y6xaAhhjnb1dM_RtTC0c'

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# Информация о боте
url = f'{MAIN_URL}/getMe'

print(url)

proxies = {
    'http': 'http://167.86.96.4:3128',
    'https': 'http://167.86.96.4:3128',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

# result = requests.get(url, proxies=proxies, headers=headers)

# pprint.pprint(result.json())

# Как понять что нам написали сообщение
# Обновления
while True:
    time.sleep(5)
    url = f'{MAIN_URL}/getUpdates'

    result = requests.get(url, proxies=proxies, headers=headers)

    pprint.pprint(result.json())

    messages = result.json()['result']

    for message in messages:
        # Как ответить на сообщение
        chat_id = message['message']['chat']['id']
        url = f'{MAIN_URL}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': 'Привет User!'
        }

        result = requests.post(url, proxies=proxies, headers=headers, params=params)
