"""Models for test instance module"""

from django.db import models

class AboutMe(models.Model):
    filed_name = models.CharField(max_length=30)
    field_title = models.CharField(max_length=80)
    field_description = models.CharField(max_length=200)

