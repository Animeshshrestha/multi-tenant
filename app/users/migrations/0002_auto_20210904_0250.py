# Generated by Django 3.0.8 on 2021-09-03 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_liked',
        ),
        migrations.AddField(
            model_name='posts',
            name='activity_type',
            field=models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1, null=True),
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_liked_users',
        ),
        migrations.AddField(
            model_name='posts',
            name='post_liked_users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_liked_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
