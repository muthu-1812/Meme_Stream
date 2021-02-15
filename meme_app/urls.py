from django.contrib import admin
from django.urls import include, path

from . import views
from .views import MemeAPIView, MemeUpdateAPIView

urlpatterns=[
    # path('mm',views.Meme_overview,name="api-overview"),
    # path('meme-list/',views.Meme_list,name="meme-list"),
    # path('meme-detail/<str:pk>/',views.Meme_detail,name="meme-detail"),
    # path('meme-create/',views.Meme_create,name="meme-create"),
    # path('meme-update/<str:pk>/',views.Meme_update,name="meme-update"),
    # path('meme-delete/<str:pk>/',views.Meme_delete,name="meme-delete"),


    # path('memes/', MemeAPIView.as_view()),  
    # path('memes/<int:id>/', MemeUpdateAPIView.as_view()),



    # path('admin/', admin.site.urls), #admin/ is for admin portal 

    #API ENDPOINT TO GET 100 MEMES AND TO POST A MEME AS WELL
    path('memes/',  MemeAPIView.as_view(), name='memes_api_list'), # api/memes - endpoint for getting and posting meme content
    
    #PATCH API ENDPOINT TO UPDATE
    path('memes/<int:id>/',MemeUpdateAPIView.as_view(),name='memes_api_id'),

    # URL FOR THE FORM TO UPLOAD A MEME
    path('memes-form/', views.memes_form, name='memes_insert'),         
    
    #THE FORM TO SEND DATE TO UPDATE A MEME
    path('memes-update/<int:id>/', views.memes_form, name='memes_update'),


    #HOMEPAGE URL WHICH DISPLAYS MEMES FOR NOW
    path('', views.memes_List, name='memes_List'), 

    # THE FRONTEND URL WHICH DISPLAYS THE MEMES
    path('memes-list/', views.memes_List, name='memes_List'), 

    # ENDPOINT TO GET THE DETAILED VIEW OF EACH MEME
    path('memes-list/<int:id>/', views.memes_json, name='meme_json'),    
    
    
    # ENDPOINT TO DELETE A MEME
    path('delete/<int:id>/',views.memes_delete,name='memes_delete')


]