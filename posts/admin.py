from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from posts.models import Post, Category

# TODO кастомизировать нормально и вывести картинки как следует

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
