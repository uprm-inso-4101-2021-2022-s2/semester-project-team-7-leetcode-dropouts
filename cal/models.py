from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Test(models.Model):

    title = models.CharField(max_length=128)
    date = models.DateTimeField('TTT')