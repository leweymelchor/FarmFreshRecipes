from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/", include("recipes.urls")),
    path("tags/", include("tags.urls")),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("recipes_list")),
        name="home",
    ),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]
