from django.conf.urls.defaults import *

# URL patterns for aboutme

urlpatterns = patterns('aboutme.views',
  # Add url patterns here
  (r'^edit$', 'edit'),
)
