from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.models import Post
from django.http import JsonResponse

@api_view(['GET'])
def CurrentUserView(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
    })

def UserPostsView(request, pk):
    posts = Post.objects.filter(author=pk).values('id', 'content', 'date', 'author')

    return JsonResponse({'posts': list(posts)})