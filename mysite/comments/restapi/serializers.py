from rest_framework import fields, serializers
from ..models import Comment, User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Serializers define the API representation.
class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'date', 'author', 'post']

#
# BEFORE:
# {"comments":[{"id":3,"content":"Second one","date":"2021-07-28T10:09:23.259094Z","author":1}]}
# AFTER:
# [{"id":3,"content":"Second one","date":"2021-07-28T13:09:23.259094+03:00","author":{"id":1,"username":"nikola-sekulov"},"post":6}]