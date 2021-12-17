from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

class Recipe(models.Model):
    
    name = models.CharField(max_length=55)
    ingredients = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField('Tag', through='recipeTag', related_name="Recipe")
    user = models.ForeignKey(User, on_delete=models.CASCADE)