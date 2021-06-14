from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.urls import reverse

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('sn-detail', kwargs={'pk': self.post_id})
    
    def __str__(self):
        return self.content