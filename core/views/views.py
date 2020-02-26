'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'

class ProjectsView(TemplateView):
	template_name = 'projects.html'

class BlogView(TemplateView):
	template_name = 'blog.html'