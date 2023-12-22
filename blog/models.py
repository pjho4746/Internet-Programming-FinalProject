from django.db import models
from django.contrib.auth.models import User
import os

from markdown import markdown
from markdownx.models import MarkdownxField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'


#<다대일관계(개발자 제공, 따로 정의)>
class Category(models.Model):
    #동일한 이름의 카테고리가 등록되지 않도록 unique=True
    name = models.CharField(max_length=50, unique=True)
    #한글 사용 가능하도록 allow_unicode=True
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    #categorys(잘못 표현), 대응되는 문구로 변경

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'


# Post 모델 만들기(여러 필드를 담음)
class Post(models.Model):
    title = models.CharField(max_length=30)
    # 방문자가 관심을 가질만한 메시지 표시
    hook_text = models.CharField(max_length=100, blank=True)
    # TextField - 무한대로 작성 가능
    content = MarkdownxField()
    # 이미지를 업로드 / 필수가 아니다 : blank=True
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # 파일을 업로드
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # 날짜&시간의 새로운 필드를 자동 생성
    updated_at = models.DateTimeField(auto_now=True)
    # 날짜&시간 auto_now_add 자동 저장
    created_at = models.DateTimeField(auto_now_add=True)

    # author
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)


    # Post의 pk(고유번호) + Post의 title
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    # (상세페이지로 이동하기 위해) 숫자를 가져옴
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 파일의 이름만 가져옴
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 확장자를 통해 이름의 문자열을 나눠 배열 만듬 -> 마지막 요소인 파일 종료를 얻어냄
    # 파이썬에서 마지막 요소는 -1
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    #아바타 보여줌
    def get_avatar_url(self):
        if self.author.socialaccount_set.exists() :
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            #return 'http://placehold.it/50x50'
            return 'https://doitdjango.com/avatar/id/417/774db7b5af91e0bb/svg/{self.author.email}/'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    #아바타 보여줌
    def get_avatar_url(self):
        if self.author.socialaccount_set.exists() :
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            #return 'http://placehold.it/50x50'
            return 'https://doitdjango.com/avatar/id/417/774db7b5af91e0bb/svg/{self.author.email}/'
