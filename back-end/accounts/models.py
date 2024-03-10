from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    school = ((1, 'student'), (2, 'teacher'))
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    choices = models.IntegerField(choices=school)

    def __str__(self) -> str:
        return self.user.username

class Group(models.Model):
    name = models.CharField(max_length = 30)
    leader = models.ForeignKey(User, related_name = 'leader', on_delete = models.CASCADE)
    student = models.ManyToManyField(User, related_name = 'student', blank=True)

    def __str__(self) -> str:
        return self.name


class WaitGroup(models.Model):
    group = models.OneToOneField(Group, related_name='waitgroup', on_delete = models.CASCADE)
    user = models.OneToOneField(User, related_name='waituser', on_delete=models.CASCADE, blank=True)
    agree = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.group.name} ( {self.user.username} )'

