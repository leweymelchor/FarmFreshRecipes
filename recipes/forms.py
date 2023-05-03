from django import forms
from recipes.models import Rating

try:
    from recipes.models import Recipe
    from recipes.models import Step
    # from recipes.models import Ingredient
    from recipes.models import FoodItem

    class RecipeForm(forms.ModelForm):
        class Meta:
            model = Recipe
            fields = [
                "name",
                "author",
                "description",
                "image",
            ]

    class StepForm(forms.ModelForm):
        class Meta:
            model = Step
            fields = [
                "recipe",
                "order",
                "directions",
                "food_items",
            ]

    class IngredientForm(forms.ModelForm):
        class Meta:
            model = Step
            fields = [
                "recipe",
                "amount",
                "measure",
                "food",
            ]

    class FoodItemForm(forms.ModelForm):
        class Meta:
            model = FoodItem
            fields = [
                "name",
                "note",
            ]

except Exception:
    pass


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
