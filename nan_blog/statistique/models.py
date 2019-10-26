from django.db import models

# Create your models here.

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True

class Visiteur_Infos(Timemodels):
    
    ip_address = models.GenericIPAddressField()
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    page_visited = models.TextField()
    reseau_mobile = models.CharField(max_length=50)
        
    def __str__(self):
        return self.ip 
    
    