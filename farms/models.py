from django.db import models
from django.contrib.auth.models import User
from accounts.models import State, District, Taluka, Village
from django.utils.translation import gettext_lazy as _

class Farm(models.Model):
    UNIT_CHOICES = [
        ("acre", _("Acre")),
        ("hectare", _("Hectare")),
        ("guntha", _("Guntha")),
    ]

    SOIL_CHOICES = [
        ("black", _("Black Soil / काळी माती")),
        ("red", _("Red Soil / लाल माती")),
        ("alluvial", _("Alluvial Soil / गाळाची माती")),
        ("laterite", _("Laterite Soil / जांभा माती")),
        ("sandy", _("Sandy Soil / वालुकामय माती")),
        ("loamy", _("Loamy Soil / पोयट्याची माती")),
        ("clay", _("Clay Soil / चिकणमाती")),
    ]

    IRRIGATION_CHOICES = [
        ("drip", _("Drip Irrigation")),
        ("sprinkler", _("Sprinkler Irrigation")),
        ("canal", _("Canal")),
        ("borewell", _("Borewell")),
        ("well", _("Well")),
        ("rainfed", _("Rainfed")),
        ("other", _("Other")),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms")
    farm_name = models.CharField(_("Farm Name"), max_length=100)
    farm_size = models.DecimalField(_("Farm Size"), max_digits=8, decimal_places=2)
    size_unit = models.CharField(_("Unit"), max_length=10, choices=UNIT_CHOICES, default="acre")

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.SET_NULL, null=True, blank=True)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, blank=True)

    soil_type = models.CharField(_("Soil Type"), max_length=20, choices=SOIL_CHOICES)
    irrigation_type = models.CharField(_("Irrigation Type"), max_length=20, choices=IRRIGATION_CHOICES)
    latitude = models.DecimalField(_("Latitude"), max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(_("Longitude"), max_digits=9, decimal_places=6, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Farm")
        verbose_name_plural = _("Farms")

    def __str__(self):
        return f"{self.farm_name} - {self.user.username}"


class Crop(models.Model):
    SEASON_CHOICES = [
        ("kharif", _("Kharif (पावसाळी)")),
        ("rabi", _("Rabi (हिवाळी)")),
        ("zaid", _("Zaid/Summer (उन्हाळी)")),
        ("perennial", _("Perennial (बहुवार्षिक)")),
    ]

    STATUS_CHOICES = [
        ("planned", _("Planned / नियोजित")),
        ("sown", _("Sown / पेरणी झाली")),
        ("growing", _("Growing / वाढीच्या टप्प्यात")),
        ("harvested", _("Harvested / काढणी झाली")),
    ]

    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="crops")
    crop_name = models.CharField(_("Crop Name"), max_length=100)
    variety = models.CharField(_("Variety / वाण"), max_length=100, blank=True, null=True)
    area_allocated = models.DecimalField(_("Area Allocated (Acres)"), max_digits=8, decimal_places=2)
    season = models.CharField(_("Season"), max_length=20, choices=SEASON_CHOICES)
    sowing_date = models.DateField(_("Sowing / Planting Date"), null=True, blank=True)
    expected_harvest_date = models.DateField(_("Expected Harvest Date"), null=True, blank=True)
    status = models.CharField(_("Crop Status"), max_length=20, choices=STATUS_CHOICES, default="sown")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Crop")
        verbose_name_plural = _("Crops")

    def __str__(self):
        return f"{self.crop_name} ({self.farm.farm_name})"