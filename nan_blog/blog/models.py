 #--------------------import--blog-----------#
import uuid
from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.utils.text import slugify
from datetime import datetime


# Create your models here.
#------------------------ blog_app_model --------------#
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True

    
class Tag(Timemodels):
    nom = models.CharField(max_length=225)
    
    def __str__(self):
        return self.nom

class Categorie(Timemodels):
    titre =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorie',)
    nom =  models.ForeignKey(User,on_delete=models.CASCADE, related_name='ctegorieuser')
    
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'

    
    def __str__(self):
        return self.titre

class Article(models.Model):
    temps_de_lecture = models.CharField(max_length=255, null=True)
    titre =  models.CharField(max_length=255)
    titre_slug = models.SlugField(max_length=255,editable=False,default=uuid.uuid4, null=True)
    description = models.TextField()
    categorie_id =  models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name="articles")
    contenu =  HTMLField('article_description', null=True)
    photo = models.ImageField(upload_to ='article')
    tag_name = models.ManyToManyField(Tag, related_name="tag_article")
    nom =  models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=False)
    nb_com = models.PositiveIntegerField(default="0",editable=False)
    nb_like = models.PositiveIntegerField(default="0",editable=False)
   
    

    @property
    def nbr_like(self):
        n = self.likes.all().count()
      
        return n

    @property
    def nbr_comment(self):
        n = self.commentaires.all().count()
      
        return n

  


    def save(self, *args, **kwargs):
        u3 = uuid.uuid3(uuid.NAMESPACE_DNS,  str(self.pk))
       
        self.titre_slug ='@'+ slugify(self.titre + str(u3) + str(self.pk)  + self.nom.username )
        self.nb_com = self.nbr_comment
        self.nb_like=self.nbr_like
        
        super(Article, self).save(*args, **kwargs)
        


    
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'
   
    def __str__(self):
        return self.titre
    
    
class Commentaire(Timemodels):
    article_id =  models.ForeignKey(Article,on_delete=models.CASCADE, related_name="commentaires")
    username =  models.ForeignKey(User,on_delete=models.CASCADE)
    contenu =  models.TextField(null=True)
    
       
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaire des postes'
    
    def __str__(self):
        return self.username.username
    
class Reply(Timemodels):
    commentaire_id =  models.ForeignKey(Commentaire,on_delete=models.CASCADE, related_name="commentaire_poster")
    username =  models.ForeignKey(User,on_delete=models.CASCADE)
    contenu =  models.TextField(null=True)
    
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'reponse aux commentaires'
    


class Favoris(Timemodels):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    favorie_categorie = models.ManyToManyField(Categorie)
    
    class Meta:
        verbose_name = 'Favoris'
        verbose_name_plural = 'Favoris des utilisateurs'


class Like(Timemodels):
    person =  models.ForeignKey(User,on_delete=models.CASCADE, related_name="likes")
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name="likes")
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    
    def __str__(self):
        return self.person
    
class serarch (Timemodels):
    query= models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_search")
    
    class Meta:
        verbose_name = 'serarch'
        verbose_name_plural = 'les recherches des utilisateurs'