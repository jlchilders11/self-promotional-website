"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .models.models import BlogEntry
from rest_framework import routers, serializers, viewsets
from .views.views import BlogEntryViewSet, CommentViewSet

app_name = 'api'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', BlogEntryViewSet)

CommentRouter = routers.DefaultRouter()
CommentRouter.register(r'', CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^blog/', include(router.urls)),
    url(r'^comment/', include(CommentRouter.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
