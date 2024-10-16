# Generated by Django 5.1.2 on 2024-10-14 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('color', models.CharField(choices=[('red', 'red'), ('black', 'black'), ('blue', 'blue'), ('green', 'green'), ('gray', 'gray'), ('pink', 'pink'), ('yellow', 'yellow')], max_length=6)),
                ('image', models.ImageField(default='projects/default/project_d.png', upload_to='projects/project/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('budget', models.PositiveBigIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('color', models.CharField(choices=[('red', 'red'), ('black', 'black'), ('blue', 'blue'), ('green', 'green'), ('gray', 'gray'), ('pink', 'pink'), ('yellow', 'yellow')], max_length=6)),
                ('image', models.ImageField(default='projects/default/project_d.png', upload_to='projects/task/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('budget', models.PositiveBigIntegerField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('color', models.CharField(choices=[('red', 'red'), ('black', 'black'), ('blue', 'blue'), ('green', 'green'), ('gray', 'gray'), ('pink', 'pink'), ('yellow', 'yellow')], max_length=6)),
                ('image', models.ImageField(default='projects/default/project_d.png', upload_to='projects/subtask/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('budget', models.PositiveBigIntegerField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.task')),
            ],
        ),
    ]
