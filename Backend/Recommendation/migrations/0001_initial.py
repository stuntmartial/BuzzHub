# Generated by Django 3.2.2 on 2021-06-17 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suggestionString', models.CharField(blank=True, max_length=500)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Profile.profilemodel')),
            ],
        ),
    ]
