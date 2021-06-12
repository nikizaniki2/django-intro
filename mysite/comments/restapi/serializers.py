from rest_framework import serializers
from ..models import Comment

# Serializers define the API representation.
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
