from django.urls import path

from posts.views import index, post, all_posts, show_category, registration, authorization


app_name = 'posts'

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_pk>', post, name='post'),
    path('all_posts', all_posts, name='posts'),
    path('category/<int:cat_pk>', show_category, name='category'),
    path('registration', registration, name='registration'),
    path('authorization', authorization, name='authorization')
]
