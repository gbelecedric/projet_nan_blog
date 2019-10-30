from django.db import models

# Create your models here.
class Visitor_Infos_user(models.Model):
    ip_address = models.GenericIPAddressField()
    page_visited = models.TextField()
    event_date =  models.DateTimeField(auto_now=True)
    
class Visitor_Infos(models.Model):
    ip_address = models.GenericIPAddressField()
    page_visited = models.TextField()
    event_date =  models.DateTimeField(auto_now=True)
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    page_visited = models.TextField()
    reseau_mobile = models.CharField(max_length=50)
    status =  models.BooleanField(default=True)
    
    