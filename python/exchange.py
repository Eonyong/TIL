import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result = exchange.text

print(f'현재 원/달러 환율은 {result}원입니다.')