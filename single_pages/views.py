from django.shortcuts import render
from blog.models import Post
# Create your views here.

#<FBV 스타일로 페이지 만들기>
#대문 페이지
def landging(request):
    #최근 포스트
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'recent_posts' : recent_posts})

#자기소개 페이지
def about_me(request):
    return render(request, 'single_pages/about_me.html')