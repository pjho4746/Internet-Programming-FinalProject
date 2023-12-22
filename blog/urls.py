from django.urls import path
from . import views

urlpatterns = [ #서버IP/blog/
    # myInternetPrj의 urls - blog의 urls - view - html 연결

    # <FBV 스타일로 페이지 만들기 - 직접 html에 연결>
    # 서버IP/blog
    #path('', views.index),
    # 서버IP/blog 상세 페이지
    #path('<int:pk>/', views.single_post_page),

    # <CBV 스타일로 페이지 만들기>
    # 블로그 목록
    path('', views.PostList.as_view()),
    # 블로그 상세 페이지
    path('<int:pk>/', views.PostDetail.as_view()),
    # 카테고리
    path('category/<str:slug>', views.category_page),
    # 태그
    path('tag/<str:slug>', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
    #수정
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    #검색 결과 (여러 가지 형태가 들어올 수 있기 때문에 변수 q)
    path('search/<str:q>/', views.PostSearch.as_view()),
]