'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ..models import models

class HomeView(TemplateView):
	template_name = 'home.html'

class ProjectsView(TemplateView):
	template_name = 'projects.html'