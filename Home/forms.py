from django import forms
from django.db import models
from django.db.models import fields
from .models import CreatorProfile, LearnerProfile, Courses, Modules, Ref, Classroom

class CreatorRegisterForm(forms.Form):
    Name = forms.CharField(max_length = 200)
    Email = forms.EmailField(max_length = 200)
    Date_Of_Birth = forms.DateField()
    City = forms.CharField(max_length = 200)
    State = forms.CharField(max_length = 200)
    Educational_Qualification = forms.CharField(max_length = 200)
    

class LearnerRegisterForm(forms.ModelForm):
    Name = forms.CharField(max_length = 200)
    Email = forms.EmailField(max_length = 200)
    Date_Of_Birth = forms.DateField()
    City = forms.CharField(max_length = 200)
    State = forms.CharField(max_length = 200)


class CourseCreationForm(forms.Form):
    Course_Name = forms.CharField(max_length = 200)
    Course_Description =  forms.CharField(widget=forms.Textarea)
    Course_Tag = forms.CharField(max_length = 200)
