from django.contrib import admin
from .models import Profile, Playlists, Songs, FollowList

admin.site.register(Profile)
# admin.site.register(LearnerProfile)
admin.site.register(Playlists)
admin.site.register(Songs)
# admin.site.register(Reviews)
admin.site.register(FollowList)
# admin.site.register(ClassroomModules)
# admin.site.register(Classroom)
