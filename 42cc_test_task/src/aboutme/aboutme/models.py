from django.db import models

# Create your models here.

class AboutMe(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
