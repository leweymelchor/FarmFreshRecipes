from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from recipes.forms import RatingForm

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


# CLASS BASED VIEWS
class PageTitleViewMixin:
    title = ""

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class RecipeCreateView(PageTitleViewMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def get_title(self):
        return "FFR - " + self.object.name


class RecipeUpdateView(PageTitleViewMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def get_title(self):
        return "FFR - " + self.object.name


class RecipeListView(PageTitleViewMixin, ListView):
    paginate_by = 8
    model = Recipe
    template_name = "recipes/list.html"
    title = "Farm Fresh Recipes"


class RecipeDetailView(PageTitleViewMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        return context

    def get_title(self):
        return "FFR - " + self.object.name


class RecipeDeleteView(PageTitleViewMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")

    def get_title(self):
        return "FFR - " + self.object.name


# FUNCTION BASED VIEWS
def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")

    return redirect("recipe_detail", pk=recipe_id)

# def create_recipe(request):
#     if request.method == "POST" and RecipeForm:
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save()
#             return redirect("recipe_detail", pk=recipe.pk)
#     elif RecipeForm:
#         form = RecipeForm()
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "recipes/new.html", context)


# def change_recipe(request, pk):
#     if Recipe and RecipeForm:
#         instance = Recipe.objects.get(pk=pk)
#         if request.method == "POST":
#             form = RecipeForm(request.POST, instance=instance)
#             if form.is_valid():
#                 form.save()
#                 return redirect("recipe_detail", pk=pk)
#         else:
#             form = RecipeForm(instance=instance)
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "recipes/edit.html", context)


# def show_recipes(request):
#     context = {
#         "recipes": Recipe.objects.all() if Recipe else [],
#     }
#     return render(request, "recipes/list.html", context)


# def show_recipe(request, pk):
#     context = {
#         "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
#         "rating_form": RatingForm(),
#     }
#     return render(request, "recipes/detail.html", context)
