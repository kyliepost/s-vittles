from django.db import models

class Tag(models.Model):
    
    description = models.TextField()