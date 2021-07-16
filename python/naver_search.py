import requests


naver_client_id = 'THoAkGM1tIsvcF9l_AZ7'
naver_client_secret = 'XlYIk_0wJB'
url = 'https://openapi.naver.com/v1/search/shop.json?query='

headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

query = 'macBook'

product = requests.get(url + query, headers = headers).json()['items'][0]

product_name = product['title']
product_price = product['lprice']
product_link = product['link']


message = f'{product_name}\n{product_price}원\n{product_link}'

print(message)