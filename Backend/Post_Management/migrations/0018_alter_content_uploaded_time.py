# Generated by Django 3.2.2 on 2021-07-03 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0017_alter_content_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 4, 0, 36, 29, 123454)),
        ),
    ]
