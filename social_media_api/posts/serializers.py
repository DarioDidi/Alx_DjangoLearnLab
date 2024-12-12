from rest_framework import serializers

from .models import Post, Comment
from accounts.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title',
                  'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    # nested serializer for the related BlogPost
    post = PostSerializer(read_only=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'content',
                  'created_at', 'updated_at', 'post']
