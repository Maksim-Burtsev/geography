from dataclasses import field
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'created_time')