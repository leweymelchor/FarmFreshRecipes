from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=200)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)

    def rating_average(self):
        return round(self.ratings.aggregate(avg_rating=Avg('value'))['avg_rating'], 1)

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
    amount = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
     )
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
    food_items = models.ManyToManyField("FoodItem", blank=True)

    def __str__(self):
        return self.recipe.name + " step " + str(self.order)


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ratings",
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.recipe} is {self.value}  Out of 5"
