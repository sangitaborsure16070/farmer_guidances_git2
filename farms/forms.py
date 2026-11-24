from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Farm, Crop
from accounts.models import District, Taluka, Village

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            "farm_name", "farm_size", "size_unit", "state",
            "district", "taluka", "village", "soil_type",
            "irrigation_type", "latitude", "longitude"
        ]
        widgets = {
            "latitude": forms.NumberInput(attrs={"step": "any"}),
            "longitude": forms.NumberInput(attrs={"step": "any"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "state" in self.data:
            try:
                state_id = int(self.data.get("state"))
                self.fields["district"].queryset = District.objects.filter(state_id=state_id)
            except (ValueError, TypeError):
                pass
        if "district" in self.data:
            try:
                district_id = int(self.data.get("district"))
                self.fields["taluka"].queryset = Taluka.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass
        if "taluka" in self.data:
            try:
                taluka_id = int(self.data.get("taluka"))
                self.fields["village"].queryset = Village.objects.filter(taluka_id=taluka_id)
            except (ValueError, TypeError):
                pass


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ["crop_name", "variety", "area_allocated", "season", "sowing_date", "expected_harvest_date", "status"]
        widgets = {
            "sowing_date": forms.DateInput(attrs={"type": "date"}),
            "expected_harvest_date": forms.DateInput(attrs={"type": "date"}),
        }