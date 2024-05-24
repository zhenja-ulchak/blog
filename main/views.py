from django.shortcuts import get_list_or_404, render
from main.models import Post, Category
from main.api_serv import api_input

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
        'category': category,
       
    }
    return render(request, 'page/home.html', context)


def post(request, slug):
    # get_list_or_404(Post, slug=slug)
    post_one = get_list_or_404(Post, slug=slug)
    return render(request, 'post/blog-single.html',  {'post_one': post_one})


def blog_api(request):
    api_cart = api_input.apifree()
    context = {
       'api_cart' : api_cart,
       
    }
    return render(request,'page/blog-grid.html', context )


def info_api(request):
    apifree_info = api_input.apifree_info()
    posts = Post.objects.all()[:2]
    context = {
       'apifree_info' : apifree_info,
       'posts' : posts
    }
    return render(request,'info/info.html', context )