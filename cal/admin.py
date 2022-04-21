from django.contrib import admin

# Register your models here.
from .models import Test, Account, Task, Pomodorout

admin.site.register(Test)
admin.site.register(Account)
admin.site.register(Task)
admin.site.register(Pomodorout)