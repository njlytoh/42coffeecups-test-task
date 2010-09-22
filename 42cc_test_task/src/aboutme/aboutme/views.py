import re

from django.shortcuts import render_to_response
from django import forms
from django.forms import ModelForm

from aboutme.models import AboutMe

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        widgets = {
           'bio': forms.Textarea(attrs={'cols': 50, 'rows': 20}),
        }

def index(request):
    aboutme = AboutMe.get_aboutme()
    return render_to_response('aboutme/index.html', {'aboutme': aboutme})

def edit(request):
    aboutme = AboutMe.get_aboutme()
    if request.method=="POST":
        form = AboutMeForm(request.POST, instance=aboutme)
        if not form.errors:
            form.save()
    else:
        form = AboutMeForm(instance=aboutme)
    return render_to_response("aboutme/edit.html", {'form': form})

