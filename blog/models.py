from django.conf import settings
from django.db import models
from django.utils import timezone



#Post 가 Model을 상속받는다. (우클릭 -> 정의 볼 수 있음) Model 속성이나 메소드를 그대로 쓸 쑤 잇음
class Post(models.Model):
    # class 는 속성
    # foreigh key 는 다른 모델을 가리키는 속성
    # on delete 는 author가 지워졌을 경우 Post 의 객체(테이블)의 데이터
    # Cascade는 author 가 지워지면 post 도 지워지게 함
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text는 블로그 본문, 요건 길이가 정해져 있지 않은 문자열을 담을 때 쓰는 필드 
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        # self 는 자기자신의 오브젝트
        self.published_date = timezone.now()
        self.save()
        
        #str(3) -> '3'
        # post = Post()
        # post.title = '게시글'
        # print(post) -> 게시글
    def __str__(self):
        return self.title