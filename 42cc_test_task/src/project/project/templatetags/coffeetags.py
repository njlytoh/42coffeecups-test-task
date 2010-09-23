from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def isactive(request, path):
    return request.path.endswith(path) and 'active' or ''
    
    
