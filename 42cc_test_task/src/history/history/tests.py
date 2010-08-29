import json

from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import Client
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from history.models import HTTPRequestHistory

class RequestFactory(Client):
    """
    Class that lets you create mock Request objects for use in testing.
    
    Usage:
    
    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})
    
    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client
    
    Once you have a request object you can pass it to any view function, 
    just as if that view had been hooked up using a URLconf.
    
    """
    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)
        ret = WSGIRequest(environ)
        ret.user = AnonymousUser()
        return ret



class AppTestCase(TestCase):
    """
    Populate this class with unit tests for your application
    """
    
    urls = 'history.test_urls'

    def testSaveRequest(self):
        rf = RequestFactory()
        get_request = rf.get('/history/test/', {'query':'test'} )

        request = HTTPRequestHistory()

        request.save_request(get_request)
        self.assertEquals('/history/test/', request.path)
        self.assertEquals( '{"query": "test"}' , request.get)

    def testRequestHistory(self):
        client = Client()
        response = client.get('/history/test_middleware', {'query': 'test'}), 
        try:
            history_object = HTTPRequestHistory.objects.get(path='/history/test_middleware')
        except ObjectDoesNotExist:
            self.fail('Request not save in the database. Object does not exists.')
        
        self.assertEquals(history_object.get, '{"query": "test"}')

