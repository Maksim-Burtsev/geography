from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from posts.models import Post, Category


def index(request):
    """Главная страница"""
    posts = Post.objects.filter(is_publish=True)
    paginator = Paginator(posts, 7)

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

def authorization(request):
    """Авторизация пользователя"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:home')

    context = {}

    context['form'] = AuthenticationForm
    return render(request, 'posts/authorization.html', context)


def registration(request):
    """Регистрация пользователя"""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('posts:home')

    context = {}
    context['title'] = 'Регистрация'

    return render(request, 'posts/registration.html', context)