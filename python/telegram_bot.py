import requests

updates = 0

while True:
    # 기본 설정
    token = '1864791201:AAF6B9qZV5FI1k_Hcf7BEUlAiwBMoaf988g' # 자신의 토큰
    url = f'https://api.telegram.org/bot{token}'

    naver_client_id = 'THoAkGM1tIsvcF9l_AZ7' #자신의 네이버 클라이언트 id
    naver_client_secret = 'XlYIk_0wJB' ##자신의 네이버 클라이언트 secret
    naver_url = 'https://openapi.naver.com/v1/search/shop.json?query='

    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
    }
    

    #chat_id 가져오기
    updates_url = f'{url}/getUpdates'
    response = requests.get(updates_url).json()

    updates_id = response.get('result')[-1].get('message').get('date')

    if updates != updates_id:
        chat_id = response.get('result')[-1].get('message').get('chat').get('id')
        text_items = response.get('result')[-1].get('message').get('text')

        lprice = '/최저가검색 '

        if text_items[:7] == lprice:
            query = text_items[7:]

            product = requests.get(naver_url + query, headers = headers).json()['items'][0]

            product_name = product['title']
            product_price = product['lprice']
            product_link = product['link']

            message = f'최저가 상품은 {product_name}입니다,\n해당 상품의 가격은 {product_price}원 입니다.\n다양한 최저가를 보려면 아래의 링크로 접속하세요.\n{product_link}'

            message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'

            requests.get(message_url)

            updates = updates_id