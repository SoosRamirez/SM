from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField()


class Trend(models.Model):
    name = models.CharField(max_length=20, verbose_name='Раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'


class Direction(models.Model):
    name = models.CharField(max_length=20, verbose_name='Раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'


class BlogPost(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, default=1, null=True)
    name = models.CharField(max_length=100)
    preview_pic = models.ImageField()
    main_pic = models.ImageField()
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, through='Like')
    views = models.IntegerField(default=0)
    read_time = models.CharField(max_length=5, default='')
    author = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    email = models.CharField(max_length=50)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


class Trainer(models.Model):
    trend = models.ForeignKey(Trend, on_delete=models.SET_NULL, null=True)
    direction = models.ManyToManyField(Direction, through='Workout')
    name = models.CharField(max_length=20, verbose_name='Имя')
    preview_pic = models.ImageField()
    main_pic = models.ImageField(default=0)
    bio = models.TextField()
    video = models.CharField(max_length=1000)
    workouts = models.IntegerField(default=0)
    programs = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'


class WorkoutProgram(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default='0')
    subscribers = models.ManyToManyField(User, through='Subscription', default=0)
    directions = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=30)
    preview_pic = models.ImageField()
    main_pic = models.ImageField()
    video = models.CharField(max_length=1000)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_created=True)
    CHOICES = [
        ('1', 'Новичек'),
        ('2', 'Любитель'),
        ('3', 'Продвинутый'),
        ('4', 'Профессионал'),
    ]
    level = models.CharField(max_length=1, choices=CHOICES)

    length = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    amount_of_workouts = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'


class ProgramLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)


class Workout(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    video = models.CharField(max_length=100)
    picture_src = models.ImageField()
    calories = models.IntegerField(default=0)
    pub_date = models.DateField(auto_created=True, default=datetime.now)
    num_in_program = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(self)
        self.trainer.workouts = self.trainer.workouts + 1
        self.program.amount_of_workouts = self.program.amount_of_workouts + 1
        self.trainer.save()
        self.program.save()

    def delete(self, *args, **kwargs):
        self.trainer.workouts = self.trainer.workouts - 1
        self.program.amount_of_workouts = self.program.amount_of_workouts - 1
        self.program.save()
        self.trainer.save()
        super(Workout, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренировка'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    workout_stopped = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(self)
        self.program.trainer.subscribers = self.program.trainer.subscribers + 1
        self.program.trainer.save()

    def delete(self, using=None, keep_parents=False):
        self.program.trainer.subscribers = self.program.trainer.subscribers - 1
        self.program.trainer.save()
