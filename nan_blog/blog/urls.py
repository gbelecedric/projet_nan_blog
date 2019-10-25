from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('category/', views.category, name='category'),
    path('archive/', views.archive, name='archive'),
    path('element/', views.element, name='element'),

]