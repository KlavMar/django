from contextlib import nullcontext
from distutils.command import upload
from tokenize import blank_re
from unicodedata import category
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Media(models.Model):
    media=models.CharField(max_length=200)
    image=models.ImageField(blank=True,null=nullcontext)

    def __str__(self):
        return self.media
  
  
class Post(models.Model):
    post_name=models.CharField(max_length=200)
    description=models.TextField()
    categories=models.ManyToManyField('Category',blank=True)
    media=models.ForeignKey('Media',on_delete=models.CASCADE,blank=True)
    date_create=models.DateField(auto_now_add=True)
    


    def __str__(self):
        return self.post_name



