from django import forms
from django.db import models
from .models import CreatorProfile, LearnerProfile

class CreatorRegister(forms.Form):
    Name = forms.CharField(max_length = 200)
    Email = forms.EmailField(max_length = 200)
    Date_Of_Birth = forms.DateField()
    City = forms.CharField(max_length = 200)
    State = forms.CharField(max_length = 200)
    Educational_Qualification = forms.CharField(max_length = 200)
    

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