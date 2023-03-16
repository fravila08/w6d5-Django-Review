from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField()
    author =  models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    
