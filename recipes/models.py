from django.db import models


# Create your models here.
class Recipe_model(models.Model):
    title = models.CharField(max_length=125)
    ingredients = models.TextField()
    recipe = models.TextField()
    notes = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
