# Generated by Django 3.2.2 on 2021-06-20 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_alter_profilemodel_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='workPosition',
            new_name='workPositionString',
        ),
    ]