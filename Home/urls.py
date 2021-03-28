from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as Homeviews

urlpatterns = [
    path('', Homeviews.home, name = 'home'),
    path('about/', Homeviews.about, name = 'about'),
    path('accounts/', include('allauth.urls')),
    path('register/', Homeviews.register, name = 'register'),
    path('learner-register/', Homeviews.LearnerRegisterHandler, name = 'learner-register'),
    path('creator-register/', Homeviews.CreatorRegisterHandler, name = 'creator-register'),
    path('profile/view/<int:pk>/', Homeviews.profile, name = 'seeprofile'),
    path('profile/follow/<int:pk>/', Homeviews.follow, name = 'follow'),
    path('profile/unfollow/<int:pk>/', Homeviews.unfollow, name = 'unfollow'),
    path('createcourse/', Homeviews.createcourse, name = 'create-course'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)