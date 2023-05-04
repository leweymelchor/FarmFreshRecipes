from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
# def show_tags(request):
#     context = {
#         "tags": Tag.objects.all() if Tag else None,
#     }
#     return render(request, "tags/list.html", context)
class PageTitleViewMixin:
    title = ""

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class TagListView(PageTitleViewMixin, ListView):
    paginate_by = 20
    model = Tag
    template_name = "tags/list.html"
    title = "Farm Fresh Recipes Tags"


class TagDetailView(PageTitleViewMixin, DetailView):
    # paginate_by = 3
    model = Tag
    template_name = "tags/detail.html"

    def get_title(self):
        return "FFR - " + self.object.name


class TagCreateView(PageTitleViewMixin, CreateView):
    model = Tag
    template_name = "tags/create.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")
    title = "FFR - New Tag"


class TagUpdateView(PageTitleViewMixin, UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")

    def get_title(self):
        return "FFR - " + self.object.name


class TagDeleteView(PageTitleViewMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")

    def get_title(self):
        return "FFR - " + self.object.name
