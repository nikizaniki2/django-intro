from ..models import Post
from comments.models import Comment
from .serializers import PostSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def PostCommentView(request, pk):
    comments = Comment.objects.filter(post_id=pk).values('id', 'content', 'date', 'author')

    return JsonResponse({'comments': list(comments)})

#     [
#     {
#         "id": 2,
#         "content": "First comment",
#         "date": "2021-07-28T13:09:15.135053+03:00",
#         "post": 5,
#         "author": 1
#     },
#     {
#         "id": 3,
#         "content": "Second one",
#         "date": "2021-07-28T13:09:23.259094+03:00",
#         "post": 6,
#         "author": 1
#     }
# ]