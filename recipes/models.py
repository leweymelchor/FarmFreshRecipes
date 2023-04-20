from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=False)
    note = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients")
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT)
    food = models.ForeignKey(FoodItem, on_delete=models.PROTECT)

    def __str__(self):
        return self.food.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")
    order = models.PositiveSmallIntegerField()
    directions = models.TextField()

    def __str__(self):
        return self.recipe.name + " step " + str(self.order)
