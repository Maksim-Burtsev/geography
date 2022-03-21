from django.db import models


class Test(models.Model):
    """Тестирование"""

    name = models.CharField('Название теста', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    """Вопрос"""
    text = models.CharField('Вопрос', max_length=255)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL,null=True,
                             related_name='questions', verbose_name='Тест')

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Ответ"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='Вопрос')
    text = models.CharField('Ответ', max_length=255)
    is_correct = models.BooleanField('Правильный')

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
