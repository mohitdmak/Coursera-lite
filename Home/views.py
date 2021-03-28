from django.shortcuts import render, redirect
from .forms import CreatorRegister, LearnerRegister
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CreatorProfile, LearnerProfile, FollowList
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

#send_mail('Welcome to the BITS Community Page','We are glad that you have joined our community. Try to answer any questions that users may post here, and also clear your doubts. \nThis was just an automated test mail to check if you can recieve announcements via mail in future. You can confirm it by replying to this email. \nLOL.\n\n <author> mohitdmak','settings.EMAIL_HOST_USER',list,fail_silently=False)
        

def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def register(request):
    if(CreatorProfile.objects.filter(creatorusr = request.user).exists() or LearnerProfile.objects.filter(learnerusr = request.user).exists()):
        messages.success(request, 'Welcome Back !')
        return redirect('home')
    messages.success(request, 'Thanks for joining, choose one path below !')
    return render(request, 'Home/register.html')

def CreatorRegisterHandler(request):
    if request.method == 'POST':
        user_form=CreatorRegister(request.POST)

        if user_form.is_valid():
            CreatorProfile.objects.create(
                creatorusr = request.user,
                Name = user_form.cleaned_data.get('Name'),
                Email = user_form.cleaned_data.get('Email'),
                Date_Of_Birth = user_form.cleaned_data.get('Date_Of_Birth'),
                City = user_form.cleaned_data.get('City'),
                State = user_form.cleaned_data.get('State'),
                Educational_Qualification = user_form.cleaned_data.get('Educational_Qualification')
            )
            username = user_form.cleaned_data.get('Name')
            messages.success(request,f'CONGRATS {username} !, Your Creator profile is now created!')
            return redirect("home")
    else:
        user_form = CreatorRegister
        context={'user_form':user_form}
        messages.success(request,f'Please complete the verification below !')
        return render(request, 'Home/Creator_Register.html', context)


def LearnerRegisterHandler(request):
    if request.method == 'POST':
        user_form = LearnerRegister(request.POST)

        if user_form.is_valid():
            LearnerProfile.objects.create(
                learnerusr = request.user,
                Name = user_form.cleaned_data.get('Name'),
                Email = user_form.cleaned_data.get('Email'),
                Date_Of_Birth = user_form.cleaned_data.get('Date_Of_Birth'),
                City = user_form.cleaned_data.get('City'),
                State = user_form.cleaned_data.get('State')
            )
            username = user_form.cleaned_data.get('Name')
            messages.success(request,f'CONGRATS {username} !, Your Learner profile is now created!')
            return redirect("home")
    else:
        user_form = LearnerRegister
        context={'user_form':user_form}
        messages.success(request,f'Please complete the verification below !')
        return render(request, 'Home/Learner_Register.html', context)

def profile(request, **kwargs):
    if User.objects.filter(id = kwargs['pk']).exists():
        usr = User.objects.filter(id = kwargs['pk'])[0]
        if CreatorProfile.objects.filter(creatorusr = usr).exists():
            if request.user.is_authenticated:
                if(FollowList.objects.filter(followings = request.user, usertofollow = usr).exists()):
                    foll = 'u'
                else:
                    foll = 'f'
                return render(request, 'Home/cprofile.html', {'profile': usr.creatorprofile, 'foll': foll})
            return render(request, 'Home/cprofile.html', {'profile': usr.creatorprofile})
        else:
            return render(request, 'Home/lprofile.html', {'profile' : usr.learnerprofile})
    else:
        messages.success(request,f'The requested User profile does not exist :(')
        return redirect('home')

@login_required()
def follow(request, **kwargs):
    usr = User.objects.filter(id = kwargs['pk'])[0]
    request.user.followings.create(usertofollow = usr)
    messages.success(request, f'You are now following {usr.creatorprofile.Name} !')
    return redirect('home')

def unfollow(request, **kwargs):
    usr = User.objects.filter(id = kwargs['pk'])[0]
    todelete = request.user.followings.filter(usertofollow = usr)
    todelete.delete()
    request.user.save()
    messages.success(request, f'You are now unfollowing {usr.creatorprofile.Name} !')
    return redirect('home')
