from django.contrib import admin
from .models import Farm, Crop

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ("farm_name", "user", "farm_size", "size_unit", "soil_type", "district")
    list_filter = ("soil_type", "irrigation_type", "district")
    search_fields = ("farm_name", "user__username")

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ("crop_name", "farm", "season", "area_allocated", "sowing_date", "status")
    list_filter = ("season", "status")
    search_fields = ("crop_name", "variety", "farm__farm_name")