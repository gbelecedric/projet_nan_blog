from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('category/', views.category, name='category'),
    path('dashborad/', views.archive, name='archive'),
    path('profile/', views.element, name='element'),

]