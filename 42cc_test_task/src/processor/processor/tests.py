from django.test import TestCase
from django.template import RequestContext
from django.http import HttpRequest

class ContextProcessorTestCase(TestCase):
    """
    Populate this class with unit tests for your application
    """
    
    urls = 'processor.test_urls'
    def testProcessor(self):
        context = RequestContext(HttpRequest())
        self.assertTrue('django_settings' in context)
        
