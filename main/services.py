from django.contrib.auth import authenticate, login

from .forms import CommentForm
from .models import Like, Subscription


def authenticate_user(request):
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        False


def add_blog_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()


def like_blog_post(request, post_id):
    if request.user.is_authenticated:
        like = Like.objects.filter(user_id=request.user.id, post_id=post_id)
        if like:
            like.delete()
        else:
            Like.objects.create(user_id=request.user.id, post_id=post_id)


def if_subscription_exist(request, program_id):
    subscriptions = Subscription.objects.all()
    for sub in subscriptions:
        if sub.program.id == program_id and sub.user_id == request.user.id:
            return True


def create_subscription(request, program_id):
    Subscription.objects.create(user_id=request.user.id, program_id=program_id, workout_stopped=0)


def purchase_process():
    # payment = Payment.create({
    #     "amount": {
    #         "value": "100.00",
    #         "currency": "RUB"
    #     },
    #     "confirmation": {
    #         "type": "redirect",
    #         "return_url": "https://www.example.com/return_url"
    #     },
    #     "capture": True,
    #     "description": "Заказ №1"
    # }, uuid.uuid4())
    return True
