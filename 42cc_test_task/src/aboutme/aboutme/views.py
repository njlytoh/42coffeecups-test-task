# Create your views here.
from django.shortcuts import render_to_response

from aboutme.models import AboutMe

def index(request):
    aboutmes = AboutMe.objects.all()
    if aboutmes:
        aboutme = aboutmes[0]
    else:
        raise Http404("Database not initialized. run \"bin/django syncdb\"")

    return render_to_response('aboutme/index.html', {'aboutme': aboutme})

def edit(request):
    aboutmes = AboutMe.objects.all()
    if aboutmes:
        aboutme = aboutmes[0]
    else:
        raise Http404("Database not initialized. run \"bin/django syncdb\"")
    return render_to_response("aboutme/edit.html", {'aboutme': aboutme})

