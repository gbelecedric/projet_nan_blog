from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:titre>', views.detail, name='detail'),
    path('category/<str:titre>', views.categorie, name='categorie'),
    path('postimage/<int:id>', views.senduserimage, name='postimage'),
    path('postreply/<int:id>', views.sendreply, name='postreply'),
    path('dashborad/', views.archive, name='archive'),
    path('profile/', views.element, name='element'),
    path('modif_profil/', views.modif_profil, name='modif_profil'),

]
  