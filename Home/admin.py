from django.contrib import admin
from .models import CreatorProfile, LearnerProfile, Courses, Modules, Ref, Classroom

admin.site.register(CreatorProfile)
admin.site.register(LearnerProfile)
admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Ref)
admin.site.register(Classroom)