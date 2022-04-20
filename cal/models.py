from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    # account_id = models.IntegerField(primary_key=True, default=)
    # Removed due to django adding it automatically
    account_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Task(models.Model):
    # task_id = models.IntegerField(primary_key=True)
    # Removed due to django adding it automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    importance_raiting = models.IntegerField(blank=True)
    due_dates = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['importance_raiting', 'complete']

    # tied_to = models.ForeignKey(Account, on_delete=models.CASCADE)
    # ~ Will be implemented later ~

class Test(models.Model):

    title = models.CharField(max_length=128)
    date = models.DateTimeField('TTT')


class Pomodorout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    paused = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.name)