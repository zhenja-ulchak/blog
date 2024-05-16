from django.shortcuts import get_list_or_404, render
from main.models import Post, Category


def home(request):
    category = Category.objects.all()
    slug = request.GET.get('category')
    posts = Post.objects.filter(category__slug=slug)
    if posts:
        posts
    else:
        posts = Post.objects.all()
    context = {
        'posts':posts,
        'category': category
    }
    return render(request, 'page/home.html', context)


def post(request, slug):
    # get_list_or_404(Post, slug=slug)
    post_one = get_list_or_404(Post, slug=slug)
    return render(request, 'post/blog-single.html',  {'post_one': post_one})