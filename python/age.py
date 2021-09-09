import requests
from bs4 import BeautifulSoup


name = 'Jeong'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

print(response)

print(f'이름: {name}\n' + '거주하고 있는 도시 수: {0}개 이상'.format(len(response['country'])))

for i in response['country']:
    if i['country_id'] == '':
        i['country_id'] = '기타'
    print('거주하고 있는 도시 id는 {0}이고 이곳에 거주할 확률은 {1:0.02f}%입니다.'.format(i['country_id'], i['probability']))