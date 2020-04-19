from .models.models import BlogEntry
from rest_framework import serializers


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BlogEntry
        fields = ['title', 'entry', 'visible', 'publish_date', 'id']
