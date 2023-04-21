from django.contrib import admin
from .models import Recipe
from .models import Measure
from .models import FoodItem
from .models import Ingredient
from .models import Step
from .models import Rating

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(Rating)
