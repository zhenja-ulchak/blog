from django.shortcuts import get_list_or_404, render
from main.models import Post, Category
from main.api_serv import api_input
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.serializer import SnippetSerializer

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

@csrf_exempt
def snippet_list(request):

    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):

    try:
        snippet = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)