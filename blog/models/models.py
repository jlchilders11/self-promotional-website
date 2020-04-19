'''folder where our models are going to live'''

from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=30)
    entry = models.TextField()
    visible = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.title

class Comment(models.Model):
	user_name = models.CharField(max_length=30)
	email = models.EmailField()
	comment = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey(BlogEntry, on_delete=models.CASCADE, related_name='comments')