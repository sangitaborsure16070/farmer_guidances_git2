from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import FarmerProfile, State, District, Taluka, Village

class FarmerRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"), max_length=30, required=True)
    last_name = forms.CharField(label=_("Last Name"), max_length=30, required=True)
    email = forms.EmailField(label=_("Email Address"), required=False)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label=_("Confirm Password"), widget=forms.PasswordInput, required=True)
    mobile_number = forms.CharField(label=_("Mobile Number"), max_length=15, required=True)

    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, label=_("State"))
    district = forms.ModelChoiceField(queryset=District.objects.none(), required=False, label=_("District"))
    taluka = forms.ModelChoiceField(queryset=Taluka.objects.none(), required=False, label=_("Taluka"))
    village = forms.ModelChoiceField(queryset=Village.objects.none(), required=False, label=_("Village"))

    class Meta:
        model = FarmerProfile
        fields = ["mobile_number", "age", "gender", "preferred_language", "state", "district", "taluka", "village"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "state" in self.data:
            try:
                state_id = int(self.data.get("state"))
                self.fields["district"].queryset = District.objects.filter(state_id=state_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.state:
            self.fields["district"].queryset = self.instance.state.districts.order_by("name")

        if "district" in self.data:
            try:
                district_id = int(self.data.get("district"))
                self.fields["taluka"].queryset = Taluka.objects.filter(district_id=district_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.district:
            self.fields["taluka"].queryset = self.instance.district.talukas.order_by("name")

        if "taluka" in self.data:
            try:
                taluka_id = int(self.data.get("taluka"))
                self.fields["village"].queryset = Village.objects.filter(taluka_id=taluka_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.taluka:
            self.fields["village"].queryset = self.instance.taluka.villages.order_by("name")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", _("Passwords do not match."))
        return cleaned_data

class FarmerProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"), max_length=30)
    last_name = forms.CharField(label=_("Last Name"), max_length=30)
    email = forms.EmailField(label=_("Email Address"), required=False)

    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, label=_("State"))
    district = forms.ModelChoiceField(queryset=District.objects.none(), required=False, label=_("District"))
    taluka = forms.ModelChoiceField(queryset=Taluka.objects.none(), required=False, label=_("Taluka"))
    village = forms.ModelChoiceField(queryset=Village.objects.none(), required=False, label=_("Village"))

    class Meta:
        model = FarmerProfile
        fields = ["mobile_number", "profile_photo", "age", "gender", "preferred_language", "state", "district", "taluka", "village"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "state" in self.data:
            try:
                state_id = int(self.data.get("state"))
                self.fields["district"].queryset = District.objects.filter(state_id=state_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.state:
            self.fields["district"].queryset = self.instance.state.districts.order_by("name")

        if "district" in self.data:
            try:
                district_id = int(self.data.get("district"))
                self.fields["taluka"].queryset = Taluka.objects.filter(district_id=district_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.district:
            self.fields["taluka"].queryset = self.instance.district.talukas.order_by("name")

        if "taluka" in self.data:
            try:
                taluka_id = int(self.data.get("taluka"))
                self.fields["village"].queryset = Village.objects.filter(taluka_id=taluka_id).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.pk and self.instance.taluka:
            self.fields["village"].queryset = self.instance.taluka.villages.order_by("name")