from django.shortcuts import render, redirect
from .forms import CreatorRegisterForm, LearnerRegisterForm, CourseCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CreatorProfile, LearnerProfile, FollowList, Courses, Modules, Ref, Classroom
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
        user_form=CreatorRegisterForm(request.POST)

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
        user_form = CreatorRegisterForm
        context={'user_form':user_form}
        messages.success(request,f'Please complete the verification below !')
        return render(request, 'Home/Creator_Register.html', context)


def LearnerRegisterHandler(request):
    if request.method == 'POST':
        user_form = LearnerRegisterForm(request.POST)

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
        user_form = LearnerRegisterForm
        context={'user_form':user_form}
        messages.success(request,f'Please complete the verification below !')
        return render(request, 'Home/Learner_Register.html', context)

def profile(request, **kwargs):
    if User.objects.filter(id = kwargs['pk']).exists():
        usr = User.objects.filter(id = kwargs['pk'])[0]
        if CreatorProfile.objects.filter(creatorusr = usr).exists():
            pic = usr.socialaccount_set.all()[0].extra_data['picture']
            if request.user.is_authenticated:
                if(FollowList.objects.filter(followings = request.user, usertofollow = usr).exists()):
                    foll = 'u'
                else:
                    foll = 'f'
                return render(request, 'Home/cprofile.html', {'profile': usr.creatorprofile, 'foll': foll, 'pic': pic})
            return render(request, 'Home/cprofile.html', {'profile': usr.creatorprofile, 'pic': pic})
        else:
            pic = usr.socialaccount_set.all()[0].extra_data['picture']
            return render(request, 'Home/lprofile.html', {'profile' : usr.learnerprofile, 'pic': pic})
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


@login_required()
def createcourse(request):
    if CreatorProfile.objects.filter(creatorusr = request.user).exists():
        if(request.method == 'POST'):
            course_form = CourseCreationForm(request.POST)

            if course_form.is_valid():
                Courses.objects.create(
                    Course_Name = course_form.cleaned_data.get('Course_Name'),
                    Course_Desc = course_form.cleaned_data.get('Course_Description'),
                    Creator = request.user,
                    Course_Tag = course_form.cleaned_data.get('Course_Tag')
                )

                messages.success(request, 'Congrats! Your Course is now Published !')
                return redirect('home')
        
        else:
            course_form = CourseCreationForm
            return render(request, 'Home/CreateCourse.html', {'course_form': course_form})
    else:
        messages.success(request, 'Sorry, you must be a verified Creator to Launch a Course.')
        return redirect('home')