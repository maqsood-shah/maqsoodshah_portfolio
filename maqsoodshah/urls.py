from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import email, index, download

app_name = 'maqsoodshah'
urlpatterns = [
  path('', index, name = 'index'),
  path('download/', download, name = 'download'),
  path('email/', email, name = 'email')
  # path('email/', emailView, name='email'),
  # path('success/', successView, name='success'),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
