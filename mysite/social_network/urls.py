from django.urls import path, include

from .views import (PostListView, PostDetailView,
 PostCreateView, PostUpdateView, PostDeleteView)

from . import views

urlpatterns = [
    path('comment/', include('comments.urls')),
    path('', PostListView.as_view(), name='sn-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='sn-detail'),
    path('post/new/', PostCreateView.as_view(), name='sn-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='sn-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='sn-delete'),
    path('about/', views.about, name='sn-about'),
    path('restapi/', include([
        path('', include('users.restapi.urls')),
        path('', include('social_network.restapi.urls')),
        path('', include('comments.restapi.urls')),
    ])),
]
