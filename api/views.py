from rest_framework import viewsets
from .models import RedditPost
from .serializers import RedditPostSerializer

class RedditPostViewSet(viewsets.ModelViewSet):
    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
