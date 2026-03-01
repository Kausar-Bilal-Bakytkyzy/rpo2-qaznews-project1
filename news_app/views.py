from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Adv
from django.db.models import Q

def home_page(request):
    host_post = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')
    advs = Adv.objects.all()[:4]
    context = {
        'hot_posts' : host_post,
        'posts' : posts,
        'advs' : advs
    }
    return render(request, 'index.html', context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'all-news.html', context)

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    context = {
        'category' : category,
        'posts' : posts
    }
    return render(request, 'news-by-category.html', context)

def search_page(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        query_lower = query.lower()
        all_posts = Post.objects.all()


        results = [
            post for post in all_posts
            if query_lower in post.title.lower() or query_lower in post.description.lower()
        ]

    context = {
        'query': query,
        'results': results,
        'total': len(results)
    }

    return render(request, 'search-results.html', context)


def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)

    other_posts = Post.objects.filter(category=post.category).exclude(pk=pk).order_by('-created_at')[:4]

    return render(request, 'read-news.html', {
        'post': post,
        'other_posts': other_posts,
    })