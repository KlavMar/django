from contextlib import nullcontext
from distutils.command import upload
from tokenize import blank_re
from unicodedata import category
from django.db import models
from tinymce.models import HTMLField

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


class Article(models.Model):
    article_name =models.CharField(max_length=100)
    content=HTMLField()
    post_pk = models.ForeignKey('Post',on_delete=models.CASCADE)
    order_list=models.IntegerField()
    publish=models.BooleanField()

    def __str__(self):
        return self.article_name

class Comment(models.Model):
    author=models.CharField(max_length=30)
    content=models.TextField()
    created_on=models.DateField(auto_now_add=True)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    approuved = models.BooleanField(default=True)

    def __str__(self):
        return self.author