# Generated by Django 3.2.2 on 2021-07-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_rename_workposition_profilemodel_workpositionstring'),
        ('Recommendation', '0002_rename_id_suggestion_suggestionid'),
    ]

    operations = [
        migrations.CreateModel(
            name='IgnoredSuggestions',
            fields=[
                ('ignoredId', models.AutoField(primary_key=True, serialize=False)),
                ('ignoredString', models.CharField(blank=True, max_length=500)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_ig', to='Profile.profilemodel')),
            ],
        ),
    ]
