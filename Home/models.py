from django.db import models
from django.contrib.auth.models import User


class CreatorProfile(models.Model):
    creatorusr = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'creatorprofile')
    Name = models.CharField(max_length = 200)
    Email = models.EmailField(max_length = 200)
    Date_Of_Birth = models.DateField(default = None)
    City = models.CharField(max_length = 200)
    State = models.CharField(max_length = 200)
    Date_Of_Joining = models.DateField(auto_now = True)
    Educational_Qualification = models.CharField(max_length = 200)
    Rating = models.IntegerField(default = 3)

class LearnerProfile(models.Model):
    learnerusr = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'learnerprofile')
    Name = models.CharField(max_length = 200)
    Email = models.EmailField(max_length = 200)
    Date_Of_Birth = models.DateField(default = None)
    City = models.CharField(max_length = 200)
    State = models.CharField(max_length = 200)
    Date_Of_Joining = models.DateField(auto_now = True)

class FollowList(models.Model):
    usertofollow = models.ForeignKey(User,related_name='followed_by',on_delete=models.CASCADE)
    followings = models.ManyToManyField(User,related_name='followings')
    def __str__(self):
        return str(self.usertofollow)
