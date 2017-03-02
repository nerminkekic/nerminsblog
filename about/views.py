from django.shortcuts import render
from django.views.generic.list import ListView
from .models import About


#This class will render about html page.
class AboutListView(ListView):
    template_name = "about/about.html"

    def get_queryset(self):
        return About.objects.get(pk=1)

