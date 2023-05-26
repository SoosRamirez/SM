from datetime import timezone

from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

# from main.models import WorkoutProgram, Workout, Subscription
from .forms import PersonalInfoForm, PersonalProgressForm
from .models import PersonalInfo, Progress
from main.models import WorkoutProgram, Workout, Subscription


def logout_user(request):
    logout(request)


def get_personal_workout(request, program_id):
    prog = WorkoutProgram.objects.get(id=program_id)
    prog.workout_stopped = get_object_or_404(Subscription, user=request.user, program_id=program_id).workout_stopped
    prog.workouts = Workout.objects.filter(program=prog)
    return prog


def get_personal_workouts(request):
    # e = WorkoutProgram.objects.filter(subscribers=request.user)
    # for i in e:
    #     i.workouts = Workout.objects.filter(program=i)
    # context = {
    #     'workout': Workout.objects,
    #     'programs': WorkoutProgram.objects.filter(subscribers=request.user)
    # }
    sub = Subscription.objects.filter(user=request.user)
    for i in sub:
        i.program.workouts = Workout.objects.filter(program=i.program)
    return sub


def update_personal_info(request):
    info = PersonalInfo.objects.filter(user=request.user)
    if request.method == "POST":
        if info:
            if request.FILES:
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                PersonalInfo.objects.filter(user=request.user).update(image=filename)
            form = PersonalInfoForm(request.POST, instance=get_object_or_404(PersonalInfo, user=request.user))
        else:
            if request.FILES:
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                PersonalInfo.objects.create(user=request.user, image=filename)
            form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()


def get_workout_program(request):
    e = WorkoutProgram.objects.filter(subscribers=request.user)
    for i in e:
        i.workouts = Workout.objects.filter(program=i)
        return e


def update_personal_progress(request):
    progress = Progress.objects.filter(user=request.user)
    if request.method == "POST":
        if request.FILES:
            cur_pic_front = request.FILES.get('cur_pic_front', False)
            cur_pic_side = request.FILES.get('cur_pic_side', False)
            cur_pic_back = request.FILES.get('cur_pic_back', False)
            fs = FileSystemStorage()
            if cur_pic_front:
                filename = fs.save(cur_pic_front.name, cur_pic_front)
                if progress:
                    prev = get_object_or_404(Progress, user=request.user).cur_pic_front.name
                    Progress.objects.filter(user=request.user).update(cur_pic_front=filename, last_update=timezone.now())
                    Progress.objects.filter(user=request.user).update(prev_pic_front=prev, last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_front=filename)
            if cur_pic_side:
                filename = fs.save(cur_pic_side.name, cur_pic_side)
                if progress:
                    prev = get_object_or_404(Progress, user=request.user).cur_pic_side.name
                    Progress.objects.filter(user=request.user).update(cur_pic_side=filename, last_update=timezone.now())
                    Progress.objects.filter(user=request.user).update(prev_pic_side=prev, last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_side=filename)
            if cur_pic_back:
                filename = fs.save(cur_pic_back.name, cur_pic_back)
                if progress:
                    prev = get_object_or_404(Progress, user=request.user).cur_pic_side.name
                    Progress.objects.filter(user=request.user).update(cur_pic_back=filename, last_update=timezone.now())
                    Progress.objects.filter(user=request.user).update(prev_pic_back=prev, last_update=timezone.now())
                else:
                    Progress.objects.create(user=request.user, cur_pic_back=filename)
        if progress:
            form = PersonalProgressForm(request.POST, instance=get_object_or_404(Progress, user=request.user))
        else:
            form = PersonalProgressForm(request.POST)
        if form.is_valid():
            form.save()
