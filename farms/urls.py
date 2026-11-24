from django.urls import path
from . import views

app_name = "farms"

urlpatterns = [
    path("", views.farm_list_view, name="farm_list"),
    path("add/", views.farm_add_view, name="farm_add"),
    path("<int:farm_id>/", views.farm_detail_view, name="farm_detail"),
    path("<int:farm_id>/edit/", views.farm_edit_view, name="farm_edit"),
    path("<int:farm_id>/add-crop/", views.crop_add_view, name="crop_add"),
]