from django.shortcuts import render, redirect
from .forms import CreatorRegister, LearnerRegister
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def register(request):
    return render(request, 'Home/register.html')

def CreatorRegisterHandler(request):
    if request.method == 'POST':
        user_form=CreatorRegister(request.POST)
        if user_form.is_valid():
            instance = user_form.save(commit=False)
            instance.creatorusr = request.user
            instance.save()
            username = user_form.cleaned_data.get('Name')
            messages.success(request,f'CONGRATS {username} !, Your profile is now created!')
            return redirect("home")
    else:
        user_form = CreatorRegister
        context={'user_form':user_form}
        messages.success(request,f'Thanks for joining, setup your profile and you will be good to go !')
        return render(request, 'Home/Creator_Register.html', context)


def LearnerRegisterHandler(request):
    if request.method == 'POST':
        user_form = LearnerRegister(request.POST)
        if user_form.is_valid():
            user_form.instance.learnerusr = request.user
            user_form.save()
            username = user_form.cleaned_data.get('Name')
            messages.success(request,f'CONGRATS {username} !, Your profile is now created!')
            return redirect("home")
    else:
        user_form = LearnerRegister
        context={'user_form':user_form}
        messages.success(request,f'Thanks for joining, setup your profile and you will be good to go !')
        return render(request, 'Home/Learner_Register.html', context)