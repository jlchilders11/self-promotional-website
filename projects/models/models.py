'''folder where our models are going to live'''

from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=30)
	last_update = models.DateField()
	read_me = models.TextField()
	url = models.URLField()

