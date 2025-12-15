from django.db import models
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="e.g., AI & DS")
    code = models.CharField(max_length=10, blank=True, help_text="Short code e.g., AIDS")

    def __str__(self):
        return self.name
    
    # Helper methods could be added here to count events (Tech: 2, Workshop: 1)