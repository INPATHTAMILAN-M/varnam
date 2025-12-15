from django.db import models
from django.utils.translation import gettext_lazy as _

class Pass(models.Model):
    """
    Represents the main pass (e.g., Platinum Pass) shown in the green header.
    """
    name = models.CharField(max_length=100, help_text="e.g., Platinum Pass")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="e.g., 500.00")
    description = models.TextField(
        help_text="e.g., for Technical events on 06.02.25, Cultural events on..."
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"



