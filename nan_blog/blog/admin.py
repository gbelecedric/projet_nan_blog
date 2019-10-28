# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'nom')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'nom',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
  
        'titre_slug',
        'id',
        'temps_de_lecture',
        'titre',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'nbr_like',
        'nbr_comment',
        'nom',
        'date_add',
        'date_update',
        'status',
      
    )
  
    list_filter = (
      
    
        'categorie_id',
        'nom',
        'date_add',
        'date_update',
        'status',
        'id',
        'temps_de_lecture',
        'titre',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'nom',
        'date_add',
        'date_update',
        'status',
        'titre_slug',
        
    )
    raw_id_fields = ('tag_name',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'contenu',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'contenu',
    )


class ReplyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'username',
        'contenu',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'username',
        'id',
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'username',
        'contenu',
    )


class FavorisAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'user')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'user',
        'id',
        'date_add',
        'date_update',
        'status',
        'user',
    )
    raw_id_fields = ('favorie_categorie',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Reply, ReplyAdmin)
_register(models.Favoris, FavorisAdmin)
