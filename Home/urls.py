from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as Homeviews

urlpatterns = [
    path('', Homeviews.home, name = 'home'),
    path('about/', Homeviews.about, name = 'about'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)