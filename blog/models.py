from django.db import models
from django.contrib.auth.models import *
from django.urls import reverse
class Category(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self):
        return self.name
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  reverse("my-articles")