# Generated by Django 3.2.2 on 2021-05-29 06:16

import Post_Management.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('original_post_flag', models.BooleanField(default=True)),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=Post_Management.models.upload_to)),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('share_count', models.IntegerField(default=0)),
                ('uploaded_time', models.DateTimeField(default=datetime.datetime(2021, 5, 29, 11, 46, 7, 145260))),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='Profile.profilemodel')),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sharedBy', to='Profile.profilemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('shareId', models.AutoField(primary_key=True, serialize=False)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SharepostId', to='Post_Management.content')),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_by', to='Profile.profilemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('likeId', models.AutoField(primary_key=True, serialize=False)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='Profile.profilemodel')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LikepostId', to='Post_Management.content')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=100)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_by', to='Profile.profilemodel')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentpostId', to='Post_Management.content')),
            ],
        ),
    ]