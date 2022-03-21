from django.contrib import admin

from questions.models import Test, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    list_display = ('text', 'test')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
