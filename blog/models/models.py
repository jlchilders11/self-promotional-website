'''folder where our models are going to live'''

from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=30)
    entry = models.TextField()
    visible = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
