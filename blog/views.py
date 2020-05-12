from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all() # blog data 
    }
    
    return render(request, 'blog/home.html', context)


def blog(request):
    context = {
        'posts': Post.objects.all() # blog data 
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



