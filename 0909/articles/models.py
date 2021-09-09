from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models.fields import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image_thumb = ProcessedImageField(
    #     blank=True,
    #     processors=[Thumbnail(200, 200)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )   # 썸네일 이미지를 생성!( 원본 이미지를 가공하여 넣기 때문에, 원본은 저장 X, 썸네일 저장O)
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')   # Pillow package 없으면 migrations 과정에서 에러가 발생
    image_thumb = ImageSpecField(
        source='image', # 원본 이미지 필드명
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90},

    )



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
