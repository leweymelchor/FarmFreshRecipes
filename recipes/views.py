from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from recipes.forms import RatingForm
from recipes.models import Recipe
# from recipes.forms import RecipeForm
# from recipes.models import Step


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
    title = "FFR - New Recipe"


class RecipeUpdateView(PageTitleViewMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def get_title(self):
        return "FFR - " + self.object.name


class RecipeListView(PageTitleViewMixin, ListView):
    paginate_by = 6
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


# NEW Step View
# class StepCreateView(PageTitleViewMixin, CreateView):
#     model = Step
#     template_name = "recipes/new.html"
#     fields = ["name", "author", "description", "image"]
#     success_url = reverse_lazy("recipes_list")
#     title = "FFR - New Recipe"


# class StepUpdateView(PageTitleViewMixin, UpdateView):
#     model = Step
#     template_name = "recipes/edit.html"
#     fields = ["name", "author", "description", "image"]
#     success_url = reverse_lazy("recipes_list")

#     def get_title(self):
#         return "FFR - " + self.object.name


# class StepDeleteView(PageTitleViewMixin, DeleteView):
#     model = Step
#     template_name = "recipes/delete.html"
#     success_url = reverse_lazy("recipes_list")

#     def get_title(self):
#         return "FFR - " + self.object.name

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
