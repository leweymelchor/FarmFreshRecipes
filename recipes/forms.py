from django import forms
from recipes.models import Rating

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


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
