# Generated by Django 3.2.2 on 2021-06-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_alter_profilemodel_educationfieldstring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='educationConcentrationString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='educationDegreeString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='educationFieldString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='educationType',
            field=models.CharField(default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='employerString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='gender',
            field=models.CharField(default='#', max_length=1),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='hometown',
            field=models.CharField(default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='languagesString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='localeString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='locality',
            field=models.CharField(default='#', max_length=50),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='school',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='workEndyearString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='workLocationString',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='workPosition',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='workStartyearString',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
