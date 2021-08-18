from rest_framework.generics import get_object_or_404
from ..models import Post
from comments.models import Comment
from .serializers import PostSerializer
from comments.restapi.serializers import CommentSerializer 
from rest_framework import viewsets
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def PostCommentView(request, pk):
    comments = Comment.objects.filter(post_id=pk).values('id', 'content', 'date', 'author')
    return Response({'comments': comments})
    # return JsonResponse({'comments': list(comments)})


class PostCommentViewSet(viewsets.ViewSet):
    def comments(self, request, pk):
        queryset = Comment.objects.filter(post_id=pk)
        # queryset = Comment.objects.all()
        # try:
        #     comments = queryset.get(post_id=pk)
        # except:
        #     return Response({"comments":[]})
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
