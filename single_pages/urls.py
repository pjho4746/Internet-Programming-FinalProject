from django.urls import path
from . import views

urlpatterns = [ #서버IP/
    # myInternetPrj의 urls - blog의 urls - view - html 연결
    #<FBV 스타일로 페이지 만들기>
    #서버IP/ (대문 페이지)
    path('', views.landging),
    #서버IP/about_me (자기소개 페이지)
    path('about_me/', views.about_me) #서버IP/about_me
]