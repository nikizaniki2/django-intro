from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'title': "Home",
        'posts': Post.objects.all()
    }
    return render(request, 'social_network/home.html', context)
def about(request):
    return render(request, 'social_network/about.html')
