from django.db import models

class Family(models.Model):
    
    name = models.CharField(max_length=55)
    bio = models.TextField()
    user = models.ForeignKey("User", on_delete=models.CASCADE)