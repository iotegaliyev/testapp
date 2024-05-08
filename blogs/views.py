from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    """
    A view set for viewing and editing blog instances.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
