# Generated by Django 3.0.8 on 2021-09-04 03:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210904_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_stat',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]