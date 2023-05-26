from django.contrib import admin

from .models import Trend, Trainer, Workout, BlogPost, Direction, Feedback, WorkoutProgram, \
    Question, Subscription, BlogComment, Like, ProgramLike

admin.site.register(Trend)
admin.site.register(Trainer)
admin.site.register(Workout)
admin.site.register(BlogPost)
admin.site.register(Direction)
admin.site.register(Feedback)
admin.site.register(WorkoutProgram)
admin.site.register(Question)
admin.site.register(Subscription)
admin.site.register(BlogComment)
admin.site.register(Like)
admin.site.register(ProgramLike)
