from django.db import models
from django.urls import reverse

class Test(models.Model):
    """Тестирование"""

    name = models.CharField('Название теста', max_length=255)
    photo = models.ImageField('Обложка теста', upload_to='test_photos',
                              blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('questions:show_test', kwargs={'test_pk':self.pk})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    """Вопрос"""
    text = models.CharField('Вопрос', max_length=255)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True,
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
