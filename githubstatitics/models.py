from django.db import models


class RepoTable(models.Model):
    name = models.CharField(max_length=50)
    size= models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    languges= models.CharField(max_length=50)
    
    
    
    

