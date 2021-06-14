from .models import Post, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.object.post_id)
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/post/{post_id}'
    model = Comment
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return