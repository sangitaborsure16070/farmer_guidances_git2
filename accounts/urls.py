from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    # Location AJAX Endpoints
    path("ajax/load-districts/", views.load_districts, name="ajax_load_districts"),
    path("ajax/load-talukas/", views.load_talukas, name="ajax_load_talukas"),
    path("ajax/load-villages/", views.load_villages, name="ajax_load_villages"),
]