from rest_framework import serializers
from ..models import Post, User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author']
        extra_kwargs = {'author': {'required': False}}