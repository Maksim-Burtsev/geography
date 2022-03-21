from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor.widgets import CKEditorWidget

from posts.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_html_photo')
    fields = ('name', 'photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=175px;')

    get_html_photo.short_description = 'Картинка'


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label='Текст')
    summary = forms.CharField(widget=CKEditorWidget(), label='Текст в ленте')

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'created_time', 'updated_time', 'is_publish')
    list_editable = ('is_publish',)

    fields = ('title', 'text', 'author', 'category',
              'photo', 'get_html_photo', 'summary', 'is_publish')

    readonly_fields = ('get_html_photo',)

    form = PostAdminForm

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=350px;')

    get_html_photo.short_description = 'Загруженное фото'
