from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from fractions import Fraction
import math


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True, max_length=200)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)

    def rating_average(self):
        try:
            return round(self.ratings.aggregate(avg_rating=Avg('value'))['avg_rating'], 1)
        except:
            return "No Ratings Yet"

    def __str__(self):
        return self.name

    def description_shortened(self):
        short = ""
        if len(str(self.description)) > 120:
            short = (str(self.description)[:120])
        else:
            short = str(self.description)
        return short


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
    amount = models.DecimalField(
        default=1,
        decimal_places=2,
        max_digits=4,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
     )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients")
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT)
    food = models.ForeignKey(FoodItem, on_delete=models.PROTECT)

    def __str__(self):
        if int(self.amount) > 1 and self.food.name == "Tomato":
            return (f'{str(self.food.name)}' + "es")
        elif int(self.amount) > 1 and self.measure.abbreviation == "x":
            return (f'{str(self.food.name)}' + "s")
        else:
            return self.food.name

    def add_s_abbreviation(self):
        if self.measure.abbreviation == "x":
            return self.measure.abbreviation
        elif int(self.amount) > 1:
            return (f'{str(self.measure.abbreviation)}' + "s")
        else:
            return self.measure.abbreviation

    def add_s_fooditem(self):
        if int(self.amount) > 1 and self.food.name == "Tomato":
            return (f'{str(self.food.name)}' + "es")
        elif int(self.amount) > 1 and self.measure.abbreviation == "x":
            return (f'{str(self.food.name)}' + "s")
        else:
            return self.food.name

    def fraction(self):
        if int(self.amount) < 1:
            return Fraction(self.amount)
        elif int(self.amount) >= 1 and self.amount % 1 != 0:
            whole_number = int(self.amount) // 1
            fraction = Fraction(self.amount) % 1
            return f'{whole_number}' + ' ' + f'{fraction}'
        else:
            return round(self.amount, 0)


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
        if self.recipe:
            return f"{self.recipe} is {self.value}  Out of 5"
