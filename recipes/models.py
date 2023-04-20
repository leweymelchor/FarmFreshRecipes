from django.db import models


# Create your models here.
class Recipe_model(models.Model):
    title = models.CharField(max_length=125)
    notes = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Measure_model(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem_model(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient_model(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe_model, on_delete=models.CASCADE,
                               related_name="ingredients")
    measure = models.ForeignKey(Measure_model, on_delete=models.PROTECT)
    food = models.ForeignKey(FoodItem_model, on_delete=models.PROTECT)

    def __str__(self):
        return self.food


class Step_model(models.Model):
    recipe = models.ForeignKey(Recipe_model, on_delete=models.CASCADE, related_name="steps")
    order = models.PositiveSmallIntegerField()
    directions = models.TextField()

    def __str__(self):
        return self.recipe
