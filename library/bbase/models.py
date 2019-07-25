from django.conf import settings
from django.db import models



class Post(models.Model):

    name_user = models.CharField(max_length=50)
    name_book = models.CharField(max_length=100)


    #def __str__(self):
     #   return self.name_user