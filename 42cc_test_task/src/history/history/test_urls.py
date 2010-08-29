from django.conf.urls.defaults import *

# URL test patterns for history. Use this file to ensure a consistent
# set of URL patterns are used when running unit tests. This test_urls
# module should be referred to by your test class.

urlpatterns = patterns('history.views',
  # Add url patterns here
  (r'^history/test_middleware', 'test_middleware'),
)
