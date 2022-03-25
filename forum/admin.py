from django.contrib import admin

from forum.models import Topic, Message

admin.site.register(Topic)
admin.site.register(Message)