from django.urls import path, include
from .views import PostViewSet, PostCommentView, PostCommentViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
# router.register(r'comments', PostCommentViewSet, basename='Commentsss')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:pk>/comments', PostCommentViewSet.as_view({'get': 'list'}), name='post-comments'),
]
