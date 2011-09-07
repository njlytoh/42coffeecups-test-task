from django.utils import simplejson as json

from django.db import models
from django.contrib.auth.models import User


class HTTPRequestHistory(models.Model):
    path = models.CharField(max_length="100", verbose_name="HTTP request path")
    method = models.CharField(max_length="10", verbose_name="HTTP reuqest method")
    get = models.CharField(max_length="100", verbose_name="HTTP request GET data")
    post = models.TextField(verbose_name="HTTP request POST data")
    cookies = models.CharField(max_length="200", verbose_name="HTTP request cookies")
    user = models.ForeignKey(User,null=True)

    def save_request(self, request):
        self.path = request.path[:100]
        self.method = request.method
        self.get = json.dumps(request.GET)
        self.post = json.dumps(request.POST)
        self.cookies = json.dumps(request.COOKIES)
        if request.user.is_authenticated():
            self.user = request.user
        else:
            self.user = None
        self.save()

