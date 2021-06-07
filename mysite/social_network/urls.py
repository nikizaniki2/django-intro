from django.urls import path

from .views import (PostListView, PostDetailView,
 PostCreateView, PostUpdateView, PostDeleteView,
 CommentCreateView, CommentUpdateView, CommentDeleteView)

from . import views
'''
class PostEndpoint:
    def get():
        Post.objects.get(id=5)
        return Response(status=200)
    
    def put(updated_fileds):
        post = Post.objects.get(id=5)
        post.content = updated_fileds["content"]
        return Response(status=204)

    def delete():
        Post.objects.delete(id=5)
        return Response(status=204)


# Tests
client = ApiClient()
response = client.get(reverse('rest-postmodel', id=5))

assert response.status_code == 200
assert response.data == { "content": "asdasd", "author": "asdaf"}

response = client.put(reverse('rest-postmodel', id=5, updated_content="Updated"))
assert response.data == { "content": "Updated", "author": "asdaf"}
assert Post.object.get(id=5).content == "Updated"

response = client.delete(reverse('rest-postmodel', id=5))
assert response.status_code == 204
assert Post.object.exists(id=5) == False
'''

rest_urls = [
    path('rest/post/<int:pk>/', PostDetailView.as_view(), name='rest-postmodel'),  # GET, PUT (UPDATE), DELETE 

]

urlpatterns = [
    path('', PostListView.as_view(), name='sn-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='sn-detail'),  # GET, PUT (UPDATE), DELETE 
    path('comment/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/new/', PostCreateView.as_view(), name='sn-create'),
    path('post/<int:pk>/comment/new', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='sn-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='sn-delete'),
    path('about/', views.about, name='sn-about'),
]