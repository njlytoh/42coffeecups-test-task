from django.db import models

from aboutme.fields import PhoneNumberField

class AboutMe(models.Model):
    given_name = models.CharField(max_length=30, verbose_name="Given name")
    middle_name = models.CharField(max_length=30, verbose_name="Middle name", blank=True)
    family_name = models.CharField(max_length=30, verbose_name="Family name")
    cell_phone = PhoneNumberField(verbose_name="Cell phone")
    home_phone = PhoneNumberField(verbose_name="Home phone", blank=True)
    bio = models.TextField(max_length=500, verbose_name="Biography")

    @property
    def full_name(self):
        return " ".join([self.given_name, self.middle_name, self.family_name])

    @classmethod
    def get_aboutme(cls):
        aboutmes = cls.objects.all()
        if aboutmes:
            aboutme = aboutmes[0]
        else:
            raise Http404("Database not initialized. run \"bin/django syncdb\"")
        return aboutme

