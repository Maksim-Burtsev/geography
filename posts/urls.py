from django.urls import path, include

from posts.views import index

urlpatterns = [
    path('', index, name='home')
]