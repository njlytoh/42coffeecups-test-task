from django.http import HttpResponse

def test_middleware(request):
    return HttpResponse("Test middleware view.")
