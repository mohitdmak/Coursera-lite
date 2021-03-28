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

class Courses(models.Model):
    Course_Name = models.CharField(max_length = 200)
    Course_Desc = models.TextField()
    Creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'createdcourses')
    Course_completed = models.BooleanField(default = False)
    Course_Tag = models.CharField(max_length = 200)

class Modules(models.Model):
    Title = models.CharField(max_length = 200)
    Content = models.TextField()
    completed = models.BooleanField(default = False)
    Course = models.ForeignKey(Courses, on_delete = models.CASCADE, related_name = 'allmodules')
    
class Ref(models.Model):
    link = models.URLField()
    module = models.ForeignKey(Modules, on_delete = models.CASCADE, related_name = 'references')

class Classroom(models.Model):
    learners = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'classes')
    courses = models.ForeignKey(Courses, on_delete = models.CASCADE, related_name = 'classrooms')