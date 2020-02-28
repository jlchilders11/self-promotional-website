from django.contrib import admin
from .models import models

class BlogEntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'publish_date', 'visible')
admin.site.register(models.BlogEntry, BlogEntryAdmin)