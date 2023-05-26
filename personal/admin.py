from django.contrib import admin

from .models import PersonalInfo, Progress, Payment

admin.site.register(PersonalInfo)
admin.site.register(Progress)
admin.site.register(Payment)
