import requests

# Бесплатные proxy
proxies = {
    'http': 'http://167.86.96.4:3128',
    'https': 'http://167.86.96.4:3128',
}

url = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36'
}

result = requests.get(url, headers=headers, proxies=proxies)
