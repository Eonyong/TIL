import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#KOSPI_now')
result = kospi.text

print(f'현재 kospi 지수는 {result}입니다.')
