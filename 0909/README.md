#### imageField

model에서 imageField 이용시 Pillow package 없으면 migrations 과정에서 에러가 발생

migrations 이후 html의 form tag에 enctype="multipart/form-data" 을 추가

views.py의 이미지를 받는 함수에 Form(*request*.POST)을 Form(*request*.POST, *request*.FILES)로 변경

그러나, 이 상태로 이미지를 업로드 하면 경로가 맞지 않아 오류가 발생

![image-20210909112622809](C:/Users/eonyo/AppData/Roaming/Typora/typora-user-images/image-20210909112622809.png)

다시 settings.py 로 가서 

```
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/
```

을 추가.... # MEDIA_ROOT랑 STATIC_URL은 다른 경로로 설정

Django의 경우, 성능을 위해 이미지를 DB에 저장하지 않고 이미지의 URL을 DB에 저장

그다음 media 폴더를 만들어준다

#### 미디어 파일 (유저가 업로드한 이미지 파일 ) 사용 방법

> 1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
>
> 2. 프로젝트 폴더의 urls.py에서 경로 설정
>
>    * \+ static(settings.MEDIA_URL, *document_root*=settings.MEDIA_ROOT)를 urlpatterns 뒤에 추가
>
>      ```python
>      from django.contrib import admin
>      from django.urls import path, include
>      from django.conf import settings
>      from django.conf.urls.static import static
>                
>      urlpatterns = [
>          path('articles/', include('articles.urls')),
>          path('admin/', admin.site.urls),
>      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>      ```
>
>      
>
> 3. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로 저장
>
>    (upload_to의 경우는 생략 가능)
>
> 4.  업로드된 파일의 상대 url은 django가 제공하는 url 속성을 이용해서 사용 (예시: article.image.url)



#### Image resizing

1. PIL or Pillow package를 설치해줍니다.
2. `pip install django-imagekit`를 통해 imagekit을 설치
3. INSTALLED_APPS에 imagekit을 추가

하고 models.py 에 코드 추가

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

image_thumb = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90},
    )
```

썸네일 이미지를 생성!( 원본 이미지를 가공하여 넣기 때문에, 원본은 저장 :x:, 썸네일 저장:o: )



#### 원본도 저장하고 썸네일도 저장하는 방식은

```python
image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')   # Pillow package 없으면 migrations 과정에서 에러가 발생
image_thumb = ImageSpecField(
    source='image', # 원본 이미지 필드명
    processors=[Thumbnail(200, 200)],
    format='JPEG',
    options={'quality': 90},
)
```



```python
def articles_image_path(instance, filename):
	return f'user_{instance.user.pk}/{filename}'
image = models.ImageField(blank=True, upload_to=articles_image_path)
# but, 지금은 local이라 로그인한 유저가 없어서 에러가 뜸
# 나중에 로그인까지 만들면 사용해보면 도리 듯 하다.
```

그러나 이렇게만 해놓으면 삭제할 때 저장된 이미지가 삭제되지 않는 문제가 있다.



지금은 괜찮지만 나중에 데이터가 쌓이다 보면 용량을 많이 먹게 된다.

#### 이번엔 파일도 지워지도록 만들어보자.

> 1. `pip install django-cleanup`을 설치한다.
> 2. INSTALLS_APPS 에 'django_cleanup'을 추가

위 방법을 해주면 삭제시 이미지도 지워진다.



