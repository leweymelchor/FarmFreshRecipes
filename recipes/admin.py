from django.contrib import admin
from .models import Recipe_model
from .models import Measure_model
from .models import FoodItem_model

# Register your models here.
admin.site.register(Recipe_model)
admin.site.register(Measure_model)
admin.site.register(FoodItem_model)
