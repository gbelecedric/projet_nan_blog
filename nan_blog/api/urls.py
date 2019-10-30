"""le_resto URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from rest_framework.routers import DefaultRouter

from .apiviews import CategorieViewSet, TagViewSet, ArticleViewSet, CommentaireViewSet, ReplyViewSet, FavorisViewSet, Visitor_InfosViewSet, MessageViewSet, NewsletterViewSet, LinkViewSet, InfoViewSet, instagram_feedViewSet, FooterViewSet, BackgroundViewSet, HomeViewSet, MembreViewSet


router = DefaultRouter()
router.register('categorie', CategorieViewSet, base_name='categorie')
router.register('tag', TagViewSet, base_name='tag')
router.register('article', ArticleViewSet, base_name='article')
router.register('commentaire', CommentaireViewSet, base_name='commentaire')
router.register('reply', ReplyViewSet, base_name='reply')
router.register('favoris', FavorisViewSet, base_name='favoris')
router.register('infovisiteur', Visitor_InfosViewSet, base_name='infovisiteur')
router.register('message', MessageViewSet, base_name='message')
router.register('newsletter', NewsletterViewSet, base_name='newsletter')
router.register('link', LinkViewSet, base_name='link')
router.register('info', InfoViewSet, base_name='info')
router.register('instagram', instagram_feedViewSet, base_name='instagram')
router.register('foot', FooterViewSet, base_name='foot')
router.register('back', BackgroundViewSet, base_name='back')
router.register('home', HomeViewSet, base_name='home')
router.register('membre', MembreViewSet, base_name='membre')

urlpatterns = [
   
]

urlpatterns += router.urls
