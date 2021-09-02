from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)  # 입력을 받을 것
    content = models.TextField()    # 입력을 받을 것
    created_at = models.DateTimeField(auto_now_add=True)    # 위에 두개 받으면 자동 생성
    updated_at = models.DateTimeField(auto_now=True)    # 위에 두개 받으면 자동 생성

    def __str__(self):
        return f'{self.pk}번 글 - {self.title} / {self.content}'