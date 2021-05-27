from django.urls import path

from .views import (PostListView, PostDetailView,
 PostCreateView, PostUpdateView, PostDeleteView,
 CommentCreateView, CommentUpdateView, CommentDeleteView)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='sn-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='sn-detail'),
    path('comment/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/new/', PostCreateView.as_view(), name='sn-create'),
    path('post/<int:pk>/comment/new', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='sn-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='sn-delete'),
    path('about/', views.about, name='sn-about'),
]