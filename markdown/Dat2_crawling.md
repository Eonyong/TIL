# python - 크롤링

1. **크롤링이란?**

   웹 페이지를 그대로 가져와서 거기서 데이터를 추출해 내는 행위다. 크롤링하는 소프트웨어는 크롤러(crawler)

   많은 언어 중에서 python이 크롤링에 많이 쓰여지고 있는 언어이다.

2.  **패키지**

   1. **`requests`**, **`BeautifulSoup(bs4)`**

      * url의 정보를 가져오고 가공하는데 쓰이는 패키지이다.

      * 많은 작성 예시가 있지만 현재 제가 사용한 방식은

        `requests.get(url).text` 와`requests.get(url).json()`을 사용했습니다.

      * 가져온 url의 형태가 json인 경우, 

        `requests.get(url).json()`을 사용하여 수집한 데이터를 좀더 편하게 볼 수 있습니다.

      * 가져온 url의 형태가 json이 아닌 경우, 

        1. `requests.get(url).test`를 사용하여 가져온 데이터를 text화

        2. `BeautifulSoup(url, 'html.parser')`코드를 이용하여 

           soup 객체로 변환

        3. `parser.select_one(html 요소)`를 이용하여 원하는 html 요소를 하나만 찾아냄

3. **마무리**

   python 폴더에 간단한 예시를 통해 확인하실 수 있습니다.

   이를 통해 보다 간단하게 웹 크롤링을 하여 원하는 정보만 얻을 수 있게 되었습니다.