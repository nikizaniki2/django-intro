from ..models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets

# ViewSets define the view behavior.
class CommentSerializer(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)