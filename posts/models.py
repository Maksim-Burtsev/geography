from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории публикаций"""
    name = models.CharField('Название', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Публикация"""
    title = models.CharField('Название', max_length=255)
    
    summary = models.TextField('Текст на главной', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория', related_name='posts')
    photo = models.ImageField('Фотография', upload_to='post_photos')

    created_time = models.DateTimeField('Дата создания', auto_now_add=True)

    updated_time = models.DateTimeField(
        'Время последнего обновления', auto_now=True)

    is_publish = models.BooleanField('Опубликовать', default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
