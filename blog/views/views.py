'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from ..models import models

class BlogDetailView(DetailView):
	model = models.BlogEntry
	template_name = 'blog.html'

class BlogListView(ListView):
	model = models.BlogEntry
	template_name = 'blogentry_list.html'

	def get_queryset(self):
		return super().get_queryset().filter(visible=True).order_by('-publish_date')
		