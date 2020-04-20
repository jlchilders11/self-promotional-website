'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from ..models.models import BlogEntry, Comment
from rest_framework import viewsets
from rest_framework import permissions
from ..serializers import BlogEntrySerializer, CommentSerializer


class BlogEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    queryset = BlogEntry.objects.all().order_by('-publish_date')
    serializer_class = BlogEntrySerializer

    def get_queryset(self):
        if not self.request.user.is_staff or not self.request.user.is_authenticated:
            return BlogEntry.objects.filter(visible=True).order_by('-publish_date')
        else:
            return BlogEntry.objects.all().order_by('-publish_date')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-publish_date')
    serializer_class = CommentSerializer

    def get_queryset(self):
        if not self.request.user.is_staff or not self.request.user.is_authenticated:
            return Comment.objects.filter(visible=True).order_by('-publish_date')
        else:
            return Comment.objects.all().order_by('-publish_date')

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
