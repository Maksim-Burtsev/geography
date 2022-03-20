from django.contrib import admin

from posts.models import Post, Category

#TODO кастомизировать нормально и вывести картинки как следует
admin.site.register(Post)
admin.site.register(Category)