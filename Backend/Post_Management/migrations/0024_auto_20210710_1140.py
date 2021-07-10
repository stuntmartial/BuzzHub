# Generated by Django 3.2.2 on 2021-07-10 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0023_alter_content_uploaded_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='original_post_flag',
        ),
        migrations.RemoveField(
            model_name='content',
            name='share_count',
        ),
        migrations.RemoveField(
            model_name='content',
            name='shared_by',
        ),
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 11, 40, 7, 615069)),
        ),
    ]
