from django.db import models
from django.utils.translation import gettext_lazy as _
from .department import Department


class Event(models.Model):

    # Choices for the main Tabs (Technical Events vs Cultural Events)
    CATEGORY_CHOICES = [
        ('TECHNICAL', 'Technical Events'),
        ('CULTURAL', 'Cultural Events'),
    ]

    # Choices for the small badges/tags inside the card (technical, workshop)
    TAG_CHOICES = [
        ('technical', 'Technical'),
        ('workshop', 'Workshop'),
        ('non_technical', 'Non-Technical'),
    ]

    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='events'
    )
    title = models.CharField(max_length=200, help_text="e.g., DataQuest - Database Querying")
    
    # Determines which Tab this appears under
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='TECHNICAL'
    )
    
    # Determines the small purple badge style
    tag = models.CharField(
        max_length=20, 
        choices=TAG_CHOICES, 
        default='technical'
    )
    
    # The value shown in green (e.g., 2500). Could be a prize pool or individual fee.
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=0, 
        null=True, 
        blank=True, 
        help_text="The amount displayed on the card (e.g., 2500)"
    )

    def __str__(self):
        return f"{self.title} ({self.department.name})"