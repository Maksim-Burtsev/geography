from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории публикаций"""
    name = models.CharField('Название', max_length=255)
    photo = models.ImageField('Фотография', upload_to='cat_photos', blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Публикация"""
    title = models.CharField('Название', max_length=255)

    text = models.TextField('Тест публикации')

    summary = models.TextField('Текст на главной', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория', related_name='posts')
    photo = models.ImageField(
        'Фотография', upload_to='post_photos', blank=True, null=True)

    created_time = models.DateTimeField('Дата создания', auto_now_add=True)

    updated_time = models.DateTimeField(
        'Время последнего обновления', auto_now=True)

    is_publish = models.BooleanField('Опубликовать', default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_pk': self.pk})

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_time']
