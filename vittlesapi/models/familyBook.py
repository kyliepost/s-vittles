from django.db import models

class familyBook(models.Model):
    
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    family = models.ForeignKey("Family", on_delete=models.CASCADE)