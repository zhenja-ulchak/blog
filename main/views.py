from django.shortcuts import render
from main.models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'page/home.html', context)
