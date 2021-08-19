from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.models import Post
from rest_framework import viewsets
from .serializers import UserPostsSerializer

@api_view(['GET'])
def CurrentUserView(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
    })

@api_view(['GET'])
def UserPostsView(request, pk):
    posts = Post.objects.filter(author=pk).values('id', 'content', 'date', 'author')

    return Response(posts)

class UserPostsViewClass(viewsets.ViewSet):
    def posts(self, request, pk):
        queryset = Post.objects.filter(author=pk)
        serializer = UserPostsSerializer(queryset, many=True)
        return Response(serializer.data)