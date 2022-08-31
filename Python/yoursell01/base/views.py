from cgitb import html
from django.shortcuts import render
from django.views.generic import TemplateView

class indexView(TemplateView):
    template_name = "index.html"
class bundesligaView(TemplateView):
    template_name = "bundesliga.html"
class menuView(TemplateView):
    template_name = "menu.html"
class premierlView(TemplateView):
    template_name = "premierl.html"
class serieAView(TemplateView):
    template_name = "serieA.html"
