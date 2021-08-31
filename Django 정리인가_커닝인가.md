# Django

* __장고란?__ :paintbrush:

  high-level __Python Web Framework__로서 사용자 친화적인 웹 프레임워크라는 뜻이다.

  기개발된 template를 사용하여 웹을 개발하여 최대한 기능 개방에 집중할 수 있도록 하는 것이 목표이다.

  

* __Framework Architecture__ :building_construction:\

  Django는 MVC Pattern을 기반으로 한 프레임워크

  그러나 Django에서는 MTV Pattern이라 부른다.

  * M (Model): 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
  * T (Template): file:page_facing_up:의 구조나 레이아웃을 정의, 실제 우리가 보는 부분을 개발하는 장소이다
  * V (View): HTTP 요청에 대해 응답하는 부분이다. M과 T를 HTTP 통신과 중개해주는 역할이라고 생각해도 될 것같다.

![img](https://t1.daumcdn.net/cfile/tistory/224E483557C7D2A52E)

* __Django 시작__

  Django를 시작하기 전에 가상환경 세팅을 먼저 진행한다.

  ```bash
  python -m venv <가상환경 이름>	# 가상환경 생성
  
  source <가상환경 이름>/Scripts/activate	# 가상환경 실행
  # deactivate 가상환경 종료
  
  pip install django	# Django package 설치
  
  django-admin startproject <Django 프로젝트 이름> .	# Django 프로젝트 생성
  
  python manage.py runserver	#	서버 실행
  ```

  이후, `http://127.0.0.1:8000` 들어가 실행이 잘 되는지 확인을 합니다.

  잘된다면 bash로 돌아가 Ctrl+C를 눌러 서버를 종료합니다.

  ```bash
  python manage.py startapp articles	# articles라는 새로운 폴더를 만들어줍니다.
  ```

  완성이 된 걸 확인하면 프로젝트 폴더 안에 존래하는 `setting.py`로 들어갑니다.

  * __:warning::warning::warning: Django는 위에서부터 차례대로 읽어오기 떄문에 (Jupyter notebook이랑 유사) 'django.contrib.*'보다 밑에 있으면 인식이 안될 수도 있습니다.__

  ```python
  INSTALLED_APPS = [
      'articles',	# 만든 app 폴더를 여기에 추가해 줍니다.
      
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  articles의 templates 폴더 내부에 html 파일을 만들어 웹을 만들면 됩니다.

  프로젝트 폴더의 `urls.py` 파일을 수정해줍니다.

  ```django
  """생략"""
  urlpatterns = [
  	path('<html 파일 이름>/', views.<html 파일 이름>)	# 경로를 추가하여 줍니다.
  ]
  ```

  `articles` 폴더 내의 `views.py` 내용을 추가합니다.

  ```python
  from django.shortcut import render
  
  def <html 파일 이름>(request):
      return render(request, '<html 파일 이름>.html')
  ```

  모두 저장한 후 서버를 실행해줍니다.

  인터넷 주소 창에 `http://127.0.0.1:8000/<html 파일 이름>` 을 검색해서 잘 만들어 졌는지 확인합니다.
