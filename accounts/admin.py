from django.contrib import admin
from .models import State, District, Taluka, Village, FarmerProfile

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "name_mr", "name_hi")

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "name_mr")
    list_filter = ("state",)
    search_fields = ("name", "name_mr")

@admin.register(Taluka)
class TalukaAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "name_mr")
    list_filter = ("district__state", "district")
    search_fields = ("name", "name_mr")

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ("name", "taluka")
    search_fields = ("name", "name_mr")

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "mobile_number", "district", "preferred_language", "created_at")
    list_filter = ("district", "preferred_language")
    search_fields = ("user__username", "user__first_name", "mobile_number")