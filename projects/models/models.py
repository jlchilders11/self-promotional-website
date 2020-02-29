'''folder where our models are going to live'''

from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=30)
	last_update = models.DateTimeField()
	read_me = models.TextField()
	url = models.URLField()
	github_id = models.UUIDField(primary_key=True)

