from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.models import Post
from rest_framework import viewsets
from .serializers import UserPostsSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def CurrentUserView(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
    })

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    # page_size_query_param = 'page_size'
    # max_page_size = 1000

class UserPostsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        author_pk = self.kwargs['pk']
        return Post.objects.filter(author=author_pk)
    serializer_class = UserPostsSerializer