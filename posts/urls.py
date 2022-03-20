from django.urls import path

from posts.views import index, post, all_posts, show_category

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_pk>', post, name='post'),
    path('all_posts', all_posts, name='posts'),
    path('category/<int:cat_pk>', show_category, name='category')
]