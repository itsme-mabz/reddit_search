from rest_framework import serializers
from .models import RedditPost

class RedditPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPost
        fields = '__all__'
