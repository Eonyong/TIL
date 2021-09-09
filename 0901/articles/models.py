from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # max_length가 필수!! 유효성 검증 -> 위젯: (클래스 변수 - 공유)
    content = models.TextField()    # max_length가 optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)