from django.db import models

class SavedMandiRate(models.Model):
    state = models.CharField(max_length=100, db_index=True)
    district = models.CharField(max_length=100, db_index=True)
    commodity = models.CharField(max_length=100, db_index=True)
    modal_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['state', 'district', 'commodity']),
        ]
        verbose_name_plural = "Saved Mandi Rates"