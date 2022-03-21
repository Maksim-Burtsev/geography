from django.urls import path

from questions.views import index_questions, show_test

app_name = 'questions'

urlpatterns = [
    path('', index_questions, name='questions'),
    path('test/<int:test_pk>', show_test, name='show_test')
]
