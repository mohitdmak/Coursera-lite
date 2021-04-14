from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Date_Of_Joining = models.DateField(auto_now=True)
    Bio = models.TextField()


class FollowList(models.Model):
    usertofollow = models.ForeignKey(
        User, related_name="followed_by", on_delete=models.CASCADE
    )
    followings = models.ManyToManyField(User, related_name="followings")

    def __str__(self):
        return str(self.usertofollow)


class Playlists(models.Model):
    Playlist_Name = models.CharField(max_length=200)
    Playlist_Desc = models.TextField()
    Creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="createdplaylists"
    )
    lastmodified = models.DateField(auto_now=True)


class Songs(models.Model):
    Title = models.CharField(max_length=200)
    plays = models.IntegerField(default=1)
    Playlist = models.ForeignKey(
        Playlists, on_delete=models.CASCADE, related_name="allsongs"
    )
    link = models.URLField()
    Creator = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="createdsongs"
    )
