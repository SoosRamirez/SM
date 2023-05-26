from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Payment, Progress, PersonalInfo
from .services import get_personal_workout, logout_user, update_personal_info, get_workout_program, \
    get_personal_workouts, update_personal_progress


@login_required
def logout_view(request):
    logout_user(request)
    return redirect('home')


@login_required
def lk(request):
    template = 'peersonal.html'
    return render(request, template)


@csrf_protect
@login_required
def personalinfo(request):
    template = 'personalinfo.html'
    update_personal_info(request)
    info = PersonalInfo.objects.filter(user=request.user)
    if info:
        context = {
            'info': get_object_or_404(PersonalInfo, user=request.user)
        }
        return render(request, template, context)
    return render(request, template)


@login_required
def personalprogramms(request):
    template = 'personalprogramms.html'
    context = {
        'list_programs': get_workout_program(request),
    }
    return render(request, template, context)


@login_required
def personalworkouts(request):
    template = 'personalworkouts.html'
    context = {
        'sub': get_personal_workouts(request)
    }
    return render(request, template, context)


@login_required
def personalworkout(request, program_id):
    template = 'personalworkout.html'
    context = {
        'program': get_personal_workout(request, program_id),
    }
    return render(request, template, context)


@csrf_protect
@login_required
def personalprogress(request):
    template = 'personalprogress.html'
    progress = Progress.objects.filter(user=request.user)
    update_personal_progress(request)
    if progress:
        context = {
            'progress': get_object_or_404(Progress, user=request.user),
        }
        return render(request, template, context)
    return render(request, template)


@login_required
def subscription(request):
    template = 'personalpayments.html'
    context = {
        'payments': Payment.objects.filter(user=request.user).order_by('date_subscribed'),
    }
    return render(request, template, context)
