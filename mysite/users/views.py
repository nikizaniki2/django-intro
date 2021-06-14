from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from posts.models import Post
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request, **kwargs):
    if not kwargs:
        user = User.objects.get(id = request.user.id)
        posts = Post.objects.filter(author = request.user.id)

        context = {
        'posts': posts,
        'title': user.get_username(),
        'profile_pk' : request.user.id,
        'username' : user.get_username()
        }
        return render(request, 'users/profile.html', context)
    
    profile_pk = kwargs.get("profile_pk")
    if request.user.is_authenticated:
        user = User.objects.get(id=profile_pk)
        posts = Post.objects.filter(author = user.id)

        context = {
        'posts': posts,
        'title': user.get_username(),
        'profile_pk' : profile_pk,
        'username' : user.get_username()
        }
        return render(request, 'users/profile.html', context)
    else:
        return redirect('login')