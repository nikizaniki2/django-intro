from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

'''
def home(request):
    context = {
        'title': "Home",
        'posts': Post.objects.all()
    }
    return render(request, 'social_network/home.html', context)
'''

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

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/'
    model = Post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return

def about(request):
    return render(request, 'social_network/about.html')
