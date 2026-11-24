from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class State(models.Model):
    name = models.CharField(_("State Name"), max_length=100, unique=True)
    name_mr = models.CharField(_("State Name (Marathi)"), max_length=100, blank=True, null=True)
    name_hi = models.CharField(_("State Name (Hindi)"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return f"{self.name} ({self.name_mr})" if self.name_mr else self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="districts")
    name = models.CharField(_("District Name"), max_length=100)
    name_mr = models.CharField(_("District Name (Marathi)"), max_length=100, blank=True, null=True)
    name_hi = models.CharField(_("District Name (Hindi)"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")
        unique_together = ("state", "name")

    def __str__(self):
        return f"{self.name} ({self.name_mr})" if self.name_mr else self.name

class Taluka(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="talukas")
    name = models.CharField(_("Taluka Name"), max_length=100)
    name_mr = models.CharField(_("Taluka Name (Marathi)"), max_length=100, blank=True, null=True)
    name_hi = models.CharField(_("Taluka Name (Hindi)"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Taluka")
        verbose_name_plural = _("Talukas")
        unique_together = ("district", "name")

    def __str__(self):
        return f"{self.name} ({self.name_mr})" if self.name_mr else self.name

class Village(models.Model):
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE, related_name="villages")
    name = models.CharField(_("Village Name"), max_length=100)
    name_mr = models.CharField(_("Village Name (Marathi)"), max_length=100, blank=True, null=True)
    name_hi = models.CharField(_("Village Name (Hindi)"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Village")
        verbose_name_plural = _("Villages")

    def __str__(self):
        return f"{self.name} ({self.name_mr})" if self.name_mr else self.name

class FarmerProfile(models.Model):
    GENDER_CHOICES = [
        ("M", _("Male")),
        ("F", _("Female")),
        ("O", _("Other")),
    ]
    
    LANG_CHOICES = [
        ("mr", _("Marathi")),
        ("en", _("English")),
        ("hi", _("Hindi")),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mobile_number = models.CharField(_("Mobile Number"), max_length=15, unique=True)
    profile_photo = models.ImageField(_("Profile Photo"), upload_to="profiles/", blank=True, null=True)
    age = models.PositiveIntegerField(_("Age"), blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.SET_NULL, null=True, blank=True)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, blank=True)
    
    preferred_language = models.CharField(_("Preferred Language"), max_length=5, choices=LANG_CHOICES, default="mr")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Farmer Profile")
        verbose_name_plural = _("Farmer Profiles")

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.mobile_number})"