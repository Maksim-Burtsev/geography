from django.urls import path

from forum.views import topics, show_topic

app_name = 'forum'

urlpatterns = [
    path('', topics, name='topics'),
    path('<int:topic_pk>', show_topic, name='show_topic')
]