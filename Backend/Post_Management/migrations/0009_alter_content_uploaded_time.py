# Generated by Django 3.2.2 on 2021-06-18 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0008_alter_content_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 12, 22, 22, 792642)),
        ),
    ]
