from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from geo import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('tests', include('questions.urls')),
    path('weather/', include('weather.urls')),
    path('forum', include('forum.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
