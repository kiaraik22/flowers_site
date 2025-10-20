from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path('posts/', views.posts, name='menu.posts'),
 path('post-detail/<str:pk>', views.post_detail, name='post_detail'),

]