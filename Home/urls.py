from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as Homeviews

urlpatterns = [
    path('', Homeviews.home, name='home'),
    path('about/', Homeviews.about, name='about'),
    path('accounts/', include('allauth.urls')),
    path('register/', Homeviews.register, name='register'),
    #path('learner-register/', Homeviews.LearnerRegisterHandler, name = 'learner-register'),
    #path('creator-register/', Homeviews.CreatorRegisterHandler, name = 'creator-register'),
    path('profile/view/<int:pk>/', Homeviews.profile, name='seeprofile'),
    path('profile/follow/<int:pk>/', Homeviews.follow, name='follow'),
    path('profile/unfollow/<int:pk>/', Homeviews.unfollow, name='unfollow'),
    path('createplaylist/', Homeviews.createplaylist, name='create-playlist'),
    path('myplaylists/', Homeviews.myplaylists, name='myplaylists'),
    path('songcreation/', Homeviews.songcreation, name='songcreation'),
    path('createsong/Playlist/<int:pk>/',
         Homeviews.createsong, name='create-song'),
    path('allplaylists/', Homeviews.allplaylists, name='allplaylists'),
    path('Playlist/details/<int:pk>/',
         Homeviews.showplaylist, name='show-playlist'),
    #path('course/enroll/<int:pk>', Homeviews.enroll, name = 'enroll'),
    #path('course/study/<int:pk>/', Homeviews.studycourse, name = 'study'),
    path('Playlist/Song/<int:pk>/', Homeviews.showsong, name='show-song'),
    #path('course/module/complete/<int:pk>/', Homeviews.completemodule, name = 'complete-module'),
    #path('course/rateandreveiw/<int:pk>/', Homeviews.rateandreview, name = 'rateandreview'),
    path('search/', Homeviews.searchbytag, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
