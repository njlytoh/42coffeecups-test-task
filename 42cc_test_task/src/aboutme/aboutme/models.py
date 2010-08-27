from django.db import models

# Create your models here.

class AboutMe(models.Model):
    given_name = models.CharField(max_length=30, verbose_name="Given name")
    middle_name = models.CharField(max_length=30, verbose_name="Middle name", blank=True)
    family_name = models.CharField(max_length=30, verbose_name="Family name")
    cell_phone = models.CharField(max_length=30, verbose_name="Cell phone")
    home_phone = models.CharField(max_length=30, verbose_name="Home phone", blank=True)
    bio = models.TextField(max_length=500, verbose_name="Biography")

    @property
    def full_name(self):
        return " ".join([self.given_name, self.middle_name, self.family_name])


