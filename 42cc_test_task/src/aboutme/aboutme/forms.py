import re

from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

from django import forms

phone_re = re.compile(r'^(\+?[\d\-\s\.]+)$')
validate_phone_number = RegexValidator(phone_re, _(u'Enter a valid phone address.'), 'invalid')

class PhoneFormField(forms.CharField):
    default_error_messages = {
        'invalid': _(u'Enter a valid phone address.'),
    }
    default_validators = [validate_phone_number]



