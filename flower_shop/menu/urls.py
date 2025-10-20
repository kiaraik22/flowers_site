from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu.index'),

    path('catalog/', views.catalog, name='menu.catalog'),

    path('flower-detail/<str:pk>', views.flower_details, name='flower_details'),
    path('order-flower/', views.order_flower, name='order_flower'),

]