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

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
# from memev2.meme_front.views import Index
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="X-Memes API",
      default_version='v6',
      description="The Meme Stream",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('meme_app.urls')),          #TO INCLUE ALL URLS FROM THE APP MEME_APP
   
    path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), #for the swagger ui
  
]

urlpatterns += staticfiles_urlpatterns()
#Refer to static files in a template