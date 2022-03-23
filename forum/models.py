from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема обсуждений"""
    name = models.CharField('Тема обсуждения', max_length=255)
    photo = models.ImageField('Фото', upload_to='topic_photo',
                              blank=True, null=True)

    def get_absolute_url(self):
        return reverse('forum:show_topic', kwargs={'topic_pk': self.pk})

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'


class Message(models.Model):
    """Сообщение/Комментарий"""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='messages')

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                              related_name='messages', verbose_name='Обсуждение')

    text = models.TextField('Текст сообщения')

    publish_time = models.DateTimeField('Время публикации', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author} {self.topic}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-publish_time']
