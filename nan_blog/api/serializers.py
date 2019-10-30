from rest_framework import serializers

from blog.models import *
from comptes.models import *
from configuration.models import *
from contact.models import *
from entreprise.models import *
from statistique.models import *
from .models import *

from drf_dynamic_fields import DynamicFieldsMixin

#=============== App Configuration ==============#

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

class instagram_feedSerializer(serializers.ModelSerializer):
    class Meta:
        model = instagram_feed
        fields = '__all__'


#=============== App entreprise ==============#

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


#=============== App Contact ==============#

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


#=============== App Statistique ==============#

class Visitor_InfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor_Infos
        fields = '__all__'


#=============== App Blog ==============#

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    commentaire_poster = ReplySerializer(many=True, required=False)
    class Meta:
        model = Commentaire
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    article_poster = CommentaireSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    tag_article = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Tag
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'

