from django.contrib import admin

# Register your models here.
from .models import Test, Account

admin.site.register(Test)
admin.site.register(Account)