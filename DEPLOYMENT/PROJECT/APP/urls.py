from django.urls import path
from . import views

urlpatterns =[
    
    
    path('', views.Deploy_9, name='Deploy_9'),
    path('Per_Database_10/', views.Per_Database_10, name='Per_Database_10'),
   
]