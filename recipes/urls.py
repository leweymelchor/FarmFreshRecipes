from django.urls import path

# IMPORTS FOR FUNCTION VIEWS
# from recipes.views import (
#     create_recipe,
#     change_recipe,
#     log_rating,
#     show_recipe,
#     show_recipes,
# )

# IMPORTS FOR CLASS VIEWS
from recipes.views import (
    RecipeCreateView,
    change_recipe,
    log_rating,
    RecipeDetailView,
    RecipeListView,
)

# URL PATTERNS FOR FUNCTION VIEWS
# urlpatterns = [
#     path("", show_recipes, name="recipes_list"),
#     path("<int:pk>/", show_recipe, name="recipe_detail"),
#     path("new/", create_recipe, name="recipe_new"),
#     path("edit/", change_recipe, name="recipe_edit"),
#     path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
# ]

# URL PATTERNS FOR CLASS VIEWS
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
