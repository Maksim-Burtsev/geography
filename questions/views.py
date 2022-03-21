from importlib.metadata import requires
from django.shortcuts import render

from questions.models import Question, Answer, Test

def index_questions(request):
    """Страница со всеми тестами"""
    tests = Test.objects.all()
    context = {'tests':tests,}
    
    return render(request, 'questions/all_tests.html', context)

def show_test(request, test_pk):
    """Страница теста"""

    if request.method == 'POST':
        print(request.POST)

    test = Test.objects.get(pk=test_pk)

    context = {'test':test}

    return render(request, 'questions/show_test.html', context)
    