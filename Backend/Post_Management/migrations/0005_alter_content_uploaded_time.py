# Generated by Django 3.2.2 on 2021-06-17 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0004_auto_20210615_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 12, 31, 4, 572340)),
        ),
    ]
