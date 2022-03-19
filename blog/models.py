from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #모댈을 정의하는 코드(모델은 객체object이다.)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자 수가 제한된 텍스트를 정의할 때 사용 ex.제목
    text = models.TextField() #글자 수에 제한이 없는 긴 텍스트를 위한 속성 ex.블로그 콘텐츠
    created_date = models.DateTimeField( #날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #Post 모델의 제목 텍스트(string)을 얻게 된다.
