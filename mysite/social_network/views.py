from django.shortcuts import render
from .models import Post
from comments.models import Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return

class PostListView(ListView):
    model = Post
    template_name = 'social_network/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 4
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # TODO: change from objects.all to objects.filter
        #context['comments'] = Comment.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # TODO: change from objects.all to objects.filter
        context['comments'] = Comment.objects.order_by('-date').filter(post=self.kwargs['pk'])
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/'
    model = Post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return

'''
def CommentDetailView(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, PostDetailView.as_view(), context)
'''
def about(request):
    return render(request, 'social_network/about.html')

'''
# serializers.py

class PostSerializer(serializer.ModelSerializer):
    model = Post


class PostView(mixins.ModelMixin):
    serializer = PostSerializer
    permmissions = (IsAuthenticatedPermisssion,)
'''