from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import PlaylistCreationForm
from .forms import RegisterForm
from .forms import SongCreationForm
from .models import FollowList
from .models import Playlists
from .models import Profile
from .models import Songs

# send_mail('Welcome to the BITS Community Page','We are glad that you have joined our community. Try to answer any questions that users may post here, and also clear your doubts. \nThis was just an automated test mail to check if you can recieve announcements via mail in future. You can confirm it by replying to this email. \nLOL.\n\n <author> mohitdmak','settings.EMAIL_HOST_USER',list,fail_silently=False)


def home(request):
    return render(request, "Home/home.html")


def about(request):
    return render(request, "Home/about.html")


def register(request):
    if Profile.objects.filter(user=request.user).exists():
        messages.success(request, "Welcome Back !")
        return redirect("home")
    else:
        if request.method == "POST":
            user_form = RegisterForm(request.POST)
            if user_form.is_valid():
                user_form.instance.user = request.user
                user_form.save()
                username = user_form.cleaned_data.get("Name")
                messages.success(
                    request,
                    f"CONGRATS {username} !, Your Creator profile is now created!",
                )
                list = [request.user.email]
                send_mail(
                    "Welcome to Coursera - Lite !",
                    "We are glad that you have joined our community.\n Make Sure to choose a path out of Creator/Learner and complete your profile in order to use the site further.\n This was just an automated test mail to check if you can recieve announcements via mail in future. You can confirm it by replying to this email.\n\n <author> mohitdmak",
                    "settings.EMAIL_HOST_USER",
                    list,
                    fail_silently=False,
                )
                return redirect("home")
        else:
            user_form = RegisterForm()
            context = {"user_form": user_form}
            messages.success(request, f"Please complete the verification below !")
            return render(request, "Home/Register.html", context)


def profile(request, **kwargs):
    if User.objects.filter(id=kwargs["pk"]).exists():
        requesteduser = User.objects.filter(id=kwargs["pk"])[0]
        if Profile.objects.filter(user=requesteduser).exists():
            pic = requesteduser.socialaccount_set.all()[0].extra_data["picture"]
            if request.user.is_authenticated:
                if FollowList.objects.filter(
                    followings=request.user, usertofollow=requesteduser
                ).exists():
                    foll = "u"
                else:
                    foll = "f"
                return render(
                    request,
                    "Home/profile.html",
                    {"profile": requesteduser.profile, "foll": foll, "pic": pic},
                )
            return render(
                request,
                "Home/profile.html",
                {"profile": requesteduser.profile, "pic": pic},
            )
        else:
            messages.success(request, f"The requested User profile does not exist :(")
            return redirect("home")
    else:
        messages.success(request, f"The requested User profile does not exist :(")
        return redirect("home")


@login_required(redirect_field_name="register")
def follow(request, **kwargs):
    usr = User.objects.filter(id=kwargs["pk"])[0]
    request.user.followings.create(usertofollow=usr)
    messages.success(request, f"You are now following {usr.profile.Name} !")
    return redirect("seeprofile", pk=usr.id)


def unfollow(request, **kwargs):
    usr = User.objects.filter(id=kwargs["pk"])[0]
    todelete = request.user.followings.filter(usertofollow=usr)
    todelete.delete()
    request.user.save()
    messages.success(request, f"You are now unfollowing {usr.profile.Name} !")
    return redirect("seeprofile", pk=usr.id)


@login_required(redirect_field_name="register")
def createplaylist(request):
    if Profile.objects.filter(user=request.user).exists():
        if request.method == "POST":
            playlist_form = PlaylistCreationForm(request.POST)
            if playlist_form.is_valid():
                playlist_form.instance.Creator = request.user
                playlist_form.save()
                messages.success(request, "Congrats! Your Playlist is now Published !")
                list = []
                for followers in request.user.followed_by.all():
                    list.append(followers.followings.all()[0].email)
                send_mail(
                    f"Creator {request.user.profile.Name} has created a New Course !",
                    f"You recieved this mail because you follow the Creator : {request.user.profile.Name}.\n You can unsubscribe by unfollowing the creator. \n\n <author> mohitdmak",
                    "settings.EMAIL_HOST_USER",
                    list,
                    fail_silently=False,
                )
                return redirect("songcreation")
        else:
            playlist_form = PlaylistCreationForm()
            return render(
                request, "Home/CreatePlaylist.html", {"playlist_form": playlist_form}
            )
    else:
        messages.success(
            request, "Sorry, you must be a verified User to Launch a Playlist."
        )
        return redirect("home")


@login_required(redirect_field_name="register")
def songcreation(request):
    if Profile.objects.filter(user=request.user).exists():
        messages.success(request, "Choose a Playlist to add a module to !")
        return redirect("myplaylists")
    else:
        messages.success(
            request, "Sorry, you must be a verified User to Create a Song."
        )
        return redirect("home")


@login_required(redirect_field_name="register")
def myplaylists(request):
    if Profile.objects.filter(user=request.user).exists():
        return render(
            request,
            "Home/myplaylists.html",
            {"playlists": request.user.createdplaylists.all()},
        )
    else:
        messages.success(
            request, "Sorry, you must be a verified User to Create a Playlists."
        )
        return redirect("home")


@login_required(redirect_field_name="register")
def createsong(request, **kwargs):
    if Profile.objects.filter(user=request.user).exists():
        if request.method == "POST":
            song_form = SongCreationForm(request.POST)
            if song_form.is_valid():
                songplaylist = Playlists.objects.filter(id=kwargs["pk"])[0]
                if songplaylist.Creator == request.user:
                    song_form.instance.Playlist = songplaylist
                    song_form.save()
                    messages.success(
                        request,
                        f"Congrats! You have added a song to playlist {songplaylist.Playlist_Name} !",
                    )
                    return redirect("myplaylists")
                else:
                    messages.success(
                        request, "You do not have access rights to this course !"
                    )
                    return redirect("songcreation")
        else:
            song_form = SongCreationForm()
            return render(request, "Home/CreateSong.html", {"song_form": song_form})
    else:
        messages.success(request, "You must be a verified User to add songs !")
        return redirect("home")


def allplaylists(request):
    return render(
        request, "Home/allplaylists.html", {"playlists": Playlists.objects.all()}
    )


def showplaylist(request, **kwargs):
    playlisttoshow = Playlists.objects.filter(id=kwargs["pk"])[0]
    pic = playlisttoshow.Creator.socialaccount_set.all()[0].extra_data["picture"]
    return render(
        request, "Home/ShowPlaylist.html", {"playlist": playlisttoshow, "pic": pic}
    )


"""
def enroll(request, **kwargs):
    coursetoenroll = Courses.objects.filter(id = kwargs['pk'])[0]
    if LearnerProfile.objects.filter(learnerusr = request.user).exists():
        Classroom.objects.create(learners = request.user, courses = coursetoenroll)
        for module in coursetoenroll.allmodules.all():
            ClassroomModules.objects.create(learners = request.user, modules = module)
        messages.success(request, 'Congrats! You have enrolled for the course!')
        return redirect('study', pk = coursetoenroll.id)
    else:
        messages.success(request, 'Being a Creator, You cannot Study Courses !')
        return redirect('home')

@login_required(redirect_field_name = 'register')
def studycourse(request, **kwargs):
    if LearnerProfile.objects.filter(learnerusr = request.user).exists():
        currentcourse = Courses.objects.filter(id = kwargs['pk'])[0]
        if Classroom.objects.filter(learners = request.user, courses = currentcourse).exists():

            mainclass = Classroom.objects.filter(learners = request.user, courses = currentcourse)[0]
            if mainclass.Course_completed == True:
                check = True
            else:
                check = False

            return render(request, 'Home/StudyCourse.html', {'course': currentcourse, 'check': check})
        else:
            messages.success(request, 'You need to first enroll for the course!')
            return redirect('show-course', pk = currentcourse.id)
    else:
        messages.success(request, 'Being a Creator, You cannot Study Courses !')
        return redirect('home')"""


@login_required(redirect_field_name="register")
def showsong(request, **kwargs):
    currentsong = Songs.objects.filter(id=kwargs["pk"])[0]
    currentsong.plays += 1
    currentsong.save()
    return render(request, "Home/PlaySong.html", {"song": currentsong})


"""
def completemodule(request, **kwargs):
    moduletocomplete = Modules.objects.filter(id = kwargs['pk'])[0]
    classroom = ClassroomModules.objects.filter(learners = request.user, modules = moduletocomplete)[0]
    classroom.completed = True
    classroom.save()
    messages.success(request, 'Congrats! You have Studied the module !')

    number = 0
    for module in moduletocomplete.Course.allmodules.all():
        check = ClassroomModules.objects.filter(learners = request.user, modules = module)[0]
        if check.completed:
            number += 1

    if number == moduletocomplete.Course.allmodules.count():
        messages.success(request, 'Congrats! You have also Completed the Course !!!')
        mainclass = Classroom.objects.filter(learners = request.user, courses = moduletocomplete.Course)[0]
        mainclass.Course_completed = True
        mainclass.save()

        return redirect('rateandreview', pk = moduletocomplete.Course.id)

    return redirect('study', pk = moduletocomplete.Course.id)

def rateandreview(request, **kwargs):
    course = Courses.objects.filter(id = kwargs['pk'])[0]
    if request.method == 'POST':
        rate_form = RateAndReviewForm(request.POST)
        if rate_form.is_valid():
            creator = course.Creator

            rated = int(rate_form.cleaned_data.get('Rate'))
            Reviews.objects.create(rating = rated, course = course)
            ratedcreator = int(rate_form.cleaned_data.get('RateCreator'))
            ReviewsCreator.objects.create(rating = ratedcreator, creator = creator)

            Review = rate_form.cleaned_data.get('Review')

            total = course.reviews.count()
            totalcreator = creator.creatorrating.count()

            new = 0
            newcreator = 0

            for x in course.reviews.all():
                new += x.rating
            for y in creator.creatorrating.all():
                newcreator += y.rating

            course.rating = new/total
            course.testimonies.create(testimony = Review)
            course.save()

            creator.creatorprofile.rating = newcreator/totalcreator
            creator.creatorprofile.save()

            messages.success(request, 'Thanks for providing your valuable feedback')
            return redirect('home')
    else:
        rate_form = RateAndReviewForm
        return render(request, 'Home/RateAndReview.html', {'rate_form': rate_form})
"""


def searchbytag(request):
    if request.method == "POST":
        search_form = SearchByTag(request.POST)

        if search_form.is_valid():
            tag = search_form.cleaned_data.get("tag")
            return render(
                request,
                "Home/searched.html",
                {"courses": Courses.objects.filter(Course_Tag__icontains=tag)},
            )

    else:
        search_form = SearchByTag
        totaltags = []
        for course in Courses.objects.all():
            totaltags.append(course.Course_Tag)

        searchedtags = set(totaltags)
        return render(
            request,
            "Home/searchbytag.html",
            {"search_form": search_form, "tags": searchedtags},
        )
