from django.urls import path

from . import views

urlpatterns = [
    path('', views.lk, name='lk'),
    path('info', views.personalinfo, name='personalinfo'),
    path('programs', views.personalprogramms, name='personalprograms'),
    path('workouts', views.personalworkouts, name='personalworkouts'),
    path('workouts/<int:program_id>', views.personalworkout, name='personalworkout'),
    path('progres', views.personalprogress, name='personalprogres'),
    path('subscription', views.subscription, name='subscription'),
    path('logout', views.logout_view, name='logout'),
]
