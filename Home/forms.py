from django import forms
from django.db import models
from .models import CreatorProfile, LearnerProfile

class CreatorRegister(forms.ModelForm):
    Date_Of_Birth = forms.DateField()
    class Meta:
        model = CreatorProfile
        fields = [
            'Name',
            'Email',
            'Date_Of_Birth',
            'City',
            'State',
            'Educational_Qualification',
        ]

class LearnerRegister(forms.ModelForm):
    class Meta:
        model = LearnerProfile
        fields = [
            'Name',
            'Email',
            'Date_Of_Birth',
            'City',
            'State',
        ]