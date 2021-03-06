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
    path('dashborads/', views.archive, name='archive'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('dashpost', views.dashpost, name='dashpost'),
    path('post_non_valider', views.dashattente, name='dashattente'),
    path('dashdetail', views.dashdetail, name='dashdetail'),
    path('error', views.error, name='error'),
    path('ajout', views.ajout, name='ajout'),
    path('postlike', views.senddata,name='postlike'),
    
    #path('modif_profil/', views.modif_profil, name='modif_profil'),

]
  