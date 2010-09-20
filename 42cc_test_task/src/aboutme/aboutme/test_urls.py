from django.conf.urls.defaults import *

# URL test patterns for aboutme. Use this file to ensure a consistent
# set of URL patterns are used when running unit tests. This test_urls
# module should be referred to by your test class.

urlpatterns = patterns('aboutme.views',
  # Add url patterns here
  (r'^aboutme/$', 'index'),
  (r'^aboutme/edit', 'edit'),
)
