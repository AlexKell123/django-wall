from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Post
from .forms import PostForm, UserRegisterForm


def all_posts(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'wall/all_posts.html', {'posts': posts, 'title': 'Wall'})

def current_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'wall/current_post.html', {'post': post})

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('all_posts')
    else:
        form = PostForm()
        return render(request, 'wall/edit_post.html', {'form': form, 'title': 'New post'})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('current_post', pk=post.pk)
        else:
            form = PostForm(instance=post)
            return render(request, 'wall/edit_post.html', {'form': form, 'title': post.title})
    else:
        messages.success(request, "You can't edit this post!")
        return redirect('current_post', pk=post.pk)

def profile(request, user_id):
    author = User.objects.get(id=user_id)
    return render(request, 'wall/profile.html', {'author': author})

def profile_posts(request, user_id):
    author = User.objects.get(id=user_id)
    posts = Post.objects.filter(author=user_id)
    return render(request, 'wall/all_posts.html', {'posts': posts, 'title': str(author) + ' posts'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})
