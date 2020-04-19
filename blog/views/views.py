'''This is where the views for this application live. All of them are class based, so that they are futureproofed and hotswappable'''
from ..models.models import BlogEntry
from rest_framework import viewsets
from rest_framework import permissions
from ..serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    queryset = BlogEntry.objects.all().order_by('-publish_date')
    serializer_class = BlogSerializer

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
