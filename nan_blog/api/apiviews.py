from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from blog.models import *
from comptes.models import *
from configuration.models import *
from contact.models import *
from entreprise.models import *
from statistique.models import *
from .models import *

from .serializers import CategorieSerializer, TagSerializer, ArticleSerializer, CommentaireSerializer, ReplySerializer, FavorisSerializer, Visiteur_InfosSerializer, MessageSerializer, NewsletterSerializer, LinkSerializer, InfoSerializer, instagram_feedSerializer, FooterSerializer, BackgroundSerializer, HomeSerializer, MembreSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer

class Visiteur_InfosViewSet(viewsets.ModelViewSet):
    queryset = Visiteur_Infos.objects.all()
    serializer_class = Visiteur_InfosSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class instagram_feedViewSet(viewsets.ModelViewSet):
    queryset = instagram_feed.objects.all()
    serializer_class = instagram_feedSerializer

class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class BackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class MembreViewSet(viewsets.ModelViewSet):
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer
