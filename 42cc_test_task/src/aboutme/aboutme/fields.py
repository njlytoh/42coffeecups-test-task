from django.db.models.fields import CharField
from django.utils.translation import gettext as _

from aboutme.forms import PhoneFormField
 
class PhoneNumberField(CharField):
    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', None) or 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': PhoneFormField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

