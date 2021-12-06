from django.db import models

class Recipe(models.Model):
    
    name = models.CharField(max_length=55)
    ingredients = models.TextField()
    description = models.TextField()