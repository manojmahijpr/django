from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostModelForm
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/post_list.html', context)


#CRUD
# Create Retrieve Update Delete

def posts_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post' : post
    }
    return render(request, 'posts/post_detail.html', context)

def posts_create(request):
    author, created = Author.objects.get_or_create(
                        user=request.user,
                        email=request.user.email,
                        cell_num=9998887771
                    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
    context = {
        'form': form
    }
    return render(request, 'posts/post_create.html', context)
