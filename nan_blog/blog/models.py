 #--------------------import--blog-----------#
from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
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
    nom =  models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'

    
    def __str__(self):
        return self.titre

class Article(models.Model):
    temps_de_lecture = models.CharField(max_length=255)
    titre =  models.CharField(max_length=255)
    description = models.TextField()
    categorie_id =  models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name="categorie")
    contenu =  HTMLField('article_description',)
    photo = models.ImageField(upload_to ='article')
    tag_name = models.ManyToManyField(Tag)
    nom =  models.ForeignKey(User,on_delete=models.CASCADE)
    nbr_comment = models.IntegerField(default="0")
    nbr_like = models.IntegerField(default="0")
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'
   
    def __str__(self):
        
        return self.titre
    
    
class Commentaire(Timemodels):
    article_id =  models.ForeignKey(Article,on_delete=models.CASCADE, related_name="article_poster")
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
    
    


   
