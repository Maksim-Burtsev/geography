from questions.models import Answer


def _get_test_result(request, test, test_pk) -> tuple:
    """Вычисляет результат прохождения теста"""

    correct_answers = Answer.objects.filter(
        question__test_id=test_pk, is_correct=True).values('id')

    correct_answers_id = [str(i['id']) for i in list(correct_answers)]

    user_answers_id = \
        [i for ans in list(dict(request.POST).values())[1:] for i in ans]

    wrong_ans_count = len(set(correct_answers_id)-set(user_answers_id))

    correct_answers_count = correct_answers.count()

    res = correct_answers_count - wrong_ans_count
    percent = round(res/correct_answers_count, 2)*100

    return (res, correct_answers_count, percent)
