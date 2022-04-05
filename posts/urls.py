from django.urls import path, include

from rest_framework import routers

from posts.views import (
    index,
    post,
    all_posts,
    show_category,
    registration,
    authorization,
    logout_user,
    PostViewSet,
)


app_name = 'posts'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_pk>/', post, name='post'),
    path('all_posts/', all_posts, name='posts'),
    path('category/<int:cat_pk>/', show_category, name='category'),
    path('registration/', registration, name='registration'),
    path('authorization/', authorization, name='authorization'),
    path('logout/', logout_user, name='logout'),
    path('api/', include(router.urls)),
]
