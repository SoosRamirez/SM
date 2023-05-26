from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from .models import WorkoutProgram, BlogPost, Trainer, Feedback, Question, Direction, Trend, Workout, Like, \
    BlogComment
from .services import add_blog_comment, like_blog_post, create_subscription, if_subscription_exist, \
    purchase_process, authenticate_user


def home(request):
    template = 'index.html'
    context = {
        "programs_list": WorkoutProgram.objects.all()[:10],
        "blog": BlogPost.objects.all()[:10],
        "trainers": Trainer.objects.order_by('subscribers'),
        'reviews': Feedback.objects.all(),
        'questions': Question.objects.all(),
    }
    return render(request, template, context)


def trainers(request):
    template = 'trainers.html'
    context = {
        'popular': Trainer.objects.order_by('subscribers')[:10],
        'all': Trainer.objects.all(),
        'directions': Direction.objects.all(),
    }
    return render(request, template, context)


def trainer(request, trainer_id):
    template = 'trainer.html'
    context = {
        'trainer': get_object_or_404(Trainer, pk=trainer_id),
        'programs': WorkoutProgram.objects.filter(trainer_id=trainer_id),
        'trainers': Trainer.objects.all(),
        'reviews': Feedback.objects.all(),
        'questions': Question.objects.all(),

    }
    return render(request, template, context)


def programs(request):
    template = 'programms.html'
    context = {
        'trend': Trend.objects.all(),
        'all': WorkoutProgram.objects.all(),
        'new': WorkoutProgram.objects.order_by('-pub_date')[:10],
        "pop": WorkoutProgram.objects.order_by('subscribers')[:10],
        'directions': Direction.objects.all(),
        'reviews': Feedback.objects.all(),
        'questions': Question.objects.all(),
    }
    return render(request, template, context)


def program(request, program_id):
    template = 'program.html'
    get_program = get_object_or_404(WorkoutProgram, pk=program_id)
    context = {
        'program': get_program,
        'workouts': Workout.objects.filter(program_id=program_id),
        'other': WorkoutProgram.objects.filter(trainer_id=get_program.trainer_id),
        'reviews': Feedback.objects.all(),
        'questions': Question.objects.all(),
    }
    return render(request, template, context)


def blog(request):
    template = 'blog.html'
    posts = BlogPost.objects.prefetch_related('likes').all()
    for i in posts:
        print(i)
        i.liked = Like.objects.filter(post=i)
    context = {
        'posts': posts
    }
    return render(request, template, context)


@csrf_protect
def blogpost(request, post_id):
    template = 'post.html'
    context = {
        'post': get_object_or_404(BlogPost, pk=post_id),
        'comments': BlogComment.objects.filter(post=post_id),
        'other_posts': BlogPost.objects.order_by('likes')
    }
    add_blog_comment(request)
    return render(request, template, context)


def like(request, post_id):
    like_blog_post(request, post_id)
    return redirect('blog')


def subscribe(request, program_id):
    if if_subscription_exist(request, program_id):
        return redirect('program', program_id)
    create_subscription(request, program_id)
    return redirect('program', program_id)


@csrf_protect
def purchase(request):
    template = 'purchase.html'
    purchase_process()
    context = {
        'reviews': Feedback.objects.all(),
        'questions': Question.objects.all()
    }
    return render(request, template, context)


@csrf_protect
def logingin(request):
    if authenticate_user(request):
        return redirect('lk')
    else:
        return redirect('start')
