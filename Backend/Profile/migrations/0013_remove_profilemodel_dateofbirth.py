# Generated by Django 3.2.2 on 2021-07-08 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0012_auto_20210708_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='dateofbirth',
        ),
    ]
