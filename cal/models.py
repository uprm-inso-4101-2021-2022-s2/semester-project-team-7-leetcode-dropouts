from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.IntegerField(primary_key=True)
    account_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Tasks(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_Title = models.CharField(max_length=128)
    task_imrating = models.IntegerField()
    tied_to = models.ForeignKey(Account, on_delete=models.CASCADE)

class Test(models.Model):

    title = models.CharField(max_length=128)
    date = models.DateTimeField('TTT')