# Generated by Django 3.0.8 on 2021-09-04 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210904_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_liked_users',
        ),
        migrations.AddField(
            model_name='activitytype',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
