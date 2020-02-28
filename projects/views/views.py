'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from django.views.generic.list import ListView

from ..models import models

class ProjectsView(ListView):
	model = models.Project
	template_name = 'projects.html'