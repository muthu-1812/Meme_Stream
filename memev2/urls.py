"""memev2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path,include
# # from meme_app.views import *\
# from memev2.meme_app.views import MemeAPIView
# from memev2.meme_app.views import MemeUpdateAPIView
# # from . import views
# from django.contrib import admin
# from django.conf.urls import url

#this enough remove top
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from memev2.meme_front.views import Index

urlpatterns = [
    # path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('',include('meme_app.urls')),          #change it to memes
    # path('',include('frontend.urls')),           #should i chenge this
    # path('', views.Index.as_view(), name='index')
]

urlpatterns += staticfiles_urlpatterns()
#Refer to static files in a template