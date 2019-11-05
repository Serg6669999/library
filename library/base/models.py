from django.db import models

class User (models.Model):

    name_user = models.CharField(max_length=50)

    def __str__(self):
        return self.name_user

class Book (models.Model):

    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title_book = models.CharField(max_length=100)

    def __str__(self):
        return self.title_book