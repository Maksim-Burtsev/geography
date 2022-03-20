from django.shortcuts import render

from posts.models import Post, Category


def index(request):
    """Главная страница"""
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def post(request, post_pk):
    """Страница публикации"""

    post = Post.objects.get(pk=post_pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/post.html', context)

def all_posts(request):
    """Страница со всеми статьями"""

    categories = Category.objects.all()

    context = {
        'categories' : categories,
    }

    return render(request, 'posts/all_posts.html', context)

def show_category(request, cat_pk):
    """Все публикации конкретной категории"""
    category = Category.objects.get(pk=cat_pk)

    context = {
        'category':category,
    }

    return render(request, 'posts/category.html', context)