from rest_framework import serializers
from posts.models import Post, User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Serializers define the API representation.
class UserPostsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date', 'author']