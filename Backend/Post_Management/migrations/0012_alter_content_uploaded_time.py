# Generated by Django 3.2.2 on 2021-06-19 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0011_alter_content_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 19, 12, 57, 23, 567173)),
        ),
    ]