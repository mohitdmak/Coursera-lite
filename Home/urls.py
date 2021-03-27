from django.urls import path, include
from . import views as Homeviews

urlpatterns = [
    path('', Homeviews.home, name = 'home'),
]