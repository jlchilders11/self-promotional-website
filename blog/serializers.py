from .models.models import BlogEntry, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user_name',
                  'email',
                  'comment',
                  'publish_date',
                  'parent',
                  ]


class BlogEntrySerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogEntry
        fields = ['title', 'entry', 'visible',
                  'publish_date', 'id', 'comments']
