import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from .models import *

# Graphene will automatically map the Article model's fields onto the ArticleNode.
# This is configured in the ArticleNode's Meta class (as you can see below)
class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)



class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['titre',]
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection



class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection




class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        # Allow for some more advanced filtering here
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class LikeNode(DjangoObjectType):
    class Meta:
        model = Like
        filter_fields = ['date_add',]
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class Query(ObjectType):
    Tag = relay.Node.Field(TagNode)
    all_Tags = DjangoFilterConnectionField(TagNode)

    Categorie = relay.Node.Field(CategorieNode)
    all_Categories = DjangoFilterConnectionField(CategorieNode)

    Article = relay.Node.Field(ArticleNode)
    all_Articles = DjangoFilterConnectionField(ArticleNode)

    Commentaire = relay.Node.Field(CommentaireNode)
    all_Commentaires = DjangoFilterConnectionField(CommentaireNode)


    Like = relay.Node.Field(LikeNode)
    all_Likes = DjangoFilterConnectionField(LikeNode)