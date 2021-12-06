from django.db import models

class recipeTag(models.Model):
    
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)