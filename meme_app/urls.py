from django.urls import path, include
from .views import MemeAPIView, MemeUpdateAPIView
from . import views
from django.contrib import admin

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


    path('memes/',  MemeAPIView.as_view(), name='memes_api_list'), # api/memes - endpoint for getting and posting meme content
    
    
    path('memes/<int:id>/',MemeUpdateAPIView.as_view(),name='memes_api_id'),

     # get and post req. for insert operation.
    path('memes-form/', views.memes_form, name='memes_insert'),         
    
    # get and post req. for update operation.
    path('memes-update/<int:id>/', views.memes_form, name='memes_update'),


    #extra url for hmepage remove after setting up homepage
    path('', views.memes_List, name='memes_List'), 

    # get req. to retrieve and display all records.
    path('memes-list/', views.memes_List, name='memes_List'), 

    # to get the desired id field.
    path('memes-list/<int:id>/', views.memes_json, name='meme_json'),    
    
    # post req. to delete a meme using it's id
    # DISABLED FOR NOW
    path('delete/<int:id>/',views.memes_delete,name='memes_delete')


]