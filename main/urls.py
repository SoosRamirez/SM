from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('programs', views.programs, name='programs'),
    path('blog/', views.blog, name='blog'),
    path('start/', views.purchase, name='start'),
    path('trainers/<int:trainer_id>', views.trainer, name='trainer'),
    path('programs/<int:program_id>', views.program, name='program'),
    path('subscribe/<int:program_id>', views.subscribe, name='subscribe'),
    path('blog/<int:post_id>', views.blogpost, name='post'),
    path('like/<int:post_id>', views.like, name='like'),
    path('login', views.logingin, name='login'),
]
