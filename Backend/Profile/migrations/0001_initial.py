# Generated by Django 3.2.2 on 2021-05-27 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('firstname', models.CharField(default='FirstName', max_length=30)),
                ('lastname', models.CharField(default='LastName', max_length=30)),
                ('nickname', models.CharField(default='NickName', max_length=30)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('curr_city', models.TextField(default='', max_length=100)),
                ('hometown', models.TextField(default='', max_length=10)),
                ('curr_workplace', models.TextField(default='', max_length=100)),
            ],
        ),
    ]
