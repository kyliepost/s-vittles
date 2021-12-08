from django.db import models
from django.contrib.auth.models import User

class Family(models.Model):
    
    name = models.CharField(max_length=55)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)