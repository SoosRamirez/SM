from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    instagram = models.CharField(max_length=20, null=True, blank=True)
    mass = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    CHOICES = [
        ('1', 'Начальный'),
        ('2', 'Средний'),
        ('3', 'Эксперт'),
    ]
    level = models.CharField(max_length=1, choices=CHOICES, default=1, blank=True)


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    mass = models.IntegerField(null=True, blank=True)
    hips = models.IntegerField(null=True, blank=True)
    arms = models.IntegerField(null=True, blank=True)
    chest = models.IntegerField(null=True, blank=True)
    legs = models.IntegerField(null=True, blank=True)
    waist = models.IntegerField(null=True, blank=True)
    prev_pic_front = models.ImageField(default='', null=True, blank=True)
    cur_pic_front = models.ImageField(default='', null=True, blank=True)
    prev_pic_back = models.ImageField(default='', null=True, blank=True)
    cur_pic_back = models.ImageField(default='', null=True, blank=True)
    prev_pic_side = models.ImageField(default='', null=True, blank=True)
    cur_pic_side = models.ImageField(default='', null=True, blank=True)
    last_update = models.DateField(default=timezone.now, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField()
    type = models.CharField(max_length=20)
    status = models.BooleanField()
    date_subscribed = models.DateField(auto_created=True)
    promo = models.CharField(max_length=20, null=True)
    sum = models.IntegerField()
    date_expired = models.DateField(null=True)
