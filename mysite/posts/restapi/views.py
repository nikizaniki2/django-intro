from ..models import Post
from comments.models import Comment
from .serializers import PostSerializer
from comments.restapi.serializers import CommentSerializer 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def PostCommentView(request, pk):
    comments = Comment.objects.filter(post_id=pk).values('id', 'content', 'date', 'author')
    return Response({'comments': comments})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2

class PostCommentViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    serializer_class = CommentSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post_id=pk)