'''Here comes definition of middleware for request hist'''

from history.models import HTTPRequestHistory


class RequestHistory(object):

    def process_request(self, request):
        history_object = HTTPRequestHistory()
        history_object.save_request(request)


        
        
        
