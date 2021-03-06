# Generated by Django 4.0.2 on 2022-04-18 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0004_pomodorout_remove_tasks_task_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['importance_raiting', 'complete']},
        ),
        migrations.AddField(
            model_name='tasks',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='assignments',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
