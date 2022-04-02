from django.shortcuts import render

from questions.models import Test
from questions.services import _get_test_result


def index_questions(request):
    """Страница со всеми тестами"""
    tests = Test.objects.all()
    context = {'tests': tests, }

    return render(request, 'questions/all_tests.html', context)


def show_test(request, test_pk):
    """Страница теста"""
    context = {}
    test = Test.objects.prefetch_related('questions__answers').get(pk=test_pk)

    if request.method == 'POST':
        res, questions, percent = _get_test_result(request, test, test_pk)
        context['res'] = res
        context['questions'] = questions
        context['percent'] = percent


    context['test'] = test

    return render(request, 'questions/show_test.html', context)
