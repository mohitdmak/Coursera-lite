from django.contrib import admin

from .models import FollowList
from .models import Playlists
from .models import Profile
from .models import Songs

admin.site.register(Profile)
# admin.site.register(LearnerProfile)
admin.site.register(Playlists)
admin.site.register(Songs)
# admin.site.register(Reviews)
admin.site.register(FollowList)
# admin.site.register(ClassroomModules)
# admin.site.register(Classroom)
