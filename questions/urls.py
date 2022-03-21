from django.urls import path

from questions.views import index_questions

app_name = 'questions'

urlpatterns = [
    path('', index_questions, name='questions')
]
