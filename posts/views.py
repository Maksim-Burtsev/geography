from django.shortcuts import render
from django.core.paginator import Paginator

from posts.models import Post, Category


def index(request):
    """Главная страница"""
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, }

    return render(request, 'posts/index.html', context)


def post(request, post_pk):
    """Страница публикации"""

    post = Post.objects.get(pk=post_pk)
    context = {'post': post, }

    return render(request, 'posts/post.html', context)


def all_posts(request):
    """Страница со всеми статьями"""

    categories = Category.objects.all()
    context = {'categories': categories, }

    return render(request, 'posts/all_posts.html', context)


def show_category(request, cat_pk):
    """Все публикации конкретной категории"""
    category = Category.objects.get(pk=cat_pk)
    context = {'category': category, }

    return render(request, 'posts/category.html', context)
