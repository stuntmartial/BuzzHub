# Generated by Django 3.2.2 on 2021-06-20 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_Management', '0016_alter_content_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 21, 42, 39, 180965)),
        ),
    ]
