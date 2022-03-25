from calendar import c
from django.shortcuts import render

from questions.models import Question, Answer, Test

def index_questions(request):
    """Страница со всеми тестами"""
    tests = Test.objects.all()
    context = {'tests':tests,}
    
    return render(request, 'questions/all_tests.html', context)

def show_test(request, test_pk):
    """Страница теста"""
    context = {}
    if request.method == 'POST':
        res, questions, percent = _get_test_result(request, test_pk)
        context['res'] = res
        context['questions'] = questions
        context['percent'] = percent
        print(res)
    test = Test.objects.get(pk=test_pk)

    context['test'] = test

    return render(request, 'questions/show_test.html', context)
    
def _get_test_result(request, test_pk) -> tuple:
    """Вычисляет результат прохождения теста"""
    test = Test.objects.get(pk=test_pk) #select
    questions = test.questions.all()

    res = 0
    for question in questions:
        correct_answers = question.answers.filter(is_correct=True)
        correct_answers_id = [str(answer.id) for answer in correct_answers]
        
        user_answers_id = dict(request.POST).get(str(question.id))   

        if correct_answers_id == user_answers_id:
            res += 1

    questions_count = questions.count()
    percent = round(res/questions_count, 2)*100

    return (res, questions_count, percent)
