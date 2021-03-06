from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from forum.models import Message, Topic
from forum.forms import MessageForm


def topics(request):
    """Страница вывода всех существуюших обсуждений"""
    topics = Topic.objects.all()
    context = {'topics': topics}

    return render(request, 'forum/topics.html', context)


def show_topic(request, topic_pk):
    """Страница обсуждения"""

    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            text = request.POST.get('text')
            topic_id = topic_pk

            Message.objects.create(
                author_id=user_id,
                text=text,
                topic_id=topic_id,
            )
            return redirect('forum:show_topic', topic_pk)

    topic = Topic.objects.prefetch_related('messages').get(pk=topic_pk)

    messages = topic.messages.all()

    paginator = Paginator(messages, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'topic': topic,
        'page_obj': page_obj,
    }

    if request.user.is_authenticated:
        form = MessageForm()
        context['form'] = form

    return render(request, 'forum/topic.html', context)
