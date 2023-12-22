"""myInternetPrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #서버IP/admin (admin url은 생성한 장고 프로젝트에서 제공)
    path('admin/', admin.site.urls),
    #서버IP/blog (blog앱에 있는 urls.py와 연결)
    path('blog/', include('blog.urls')),
    #서버IP/blog (single_pages앱에 있는 urls.py와 연결)
    path('', include('single_pages.urls')),

    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')),
]

#서버IP/media/
#기존에 추가 / 이미지도 static파일
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)