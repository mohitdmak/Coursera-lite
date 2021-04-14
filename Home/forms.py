from django import forms
from django.db import models
from django.db.models import fields
from .models import Profile, Playlists, Songs, FollowList


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'Name',
            'Email',
            'Bio'
        ]


"""
class LearnerRegisterForm(forms.ModelForm):
    class Meta:
        model = LearnerProfile
        fields = [
            'Name',
            'Email',
            'Date_Of_Birth',
            'City',
            'State'
        ]
"""


class PlaylistCreationForm(forms.ModelForm):
    class Meta:
        model = Playlists
        fields = [
            'Playlist_Name',
            'Playlist_Desc'
        ]


class SongCreationForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = [
            'Title',
            'link'
        ]


"""
class RateAndReviewForm(forms.Form):
    ratechoices = [(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5')]
    RateCreator = forms.CharField(label = 'Rate the instructor out of 5 (On the Basis of the ease with you understood the concepts) : ', widget = forms.Select(choices = ratechoices))
    Rate = forms.CharField(label = 'Rate the course out of 5 (On the Basis of the structure and Quality of Content Presented): ', widget = forms.Select(choices = ratechoices))
    Review = forms.CharField(widget = forms.Textarea)

class SearchByTag(forms.Form):
    tag = forms.CharField(max_length = 200)"""
