# Generated by Django 4.1.4 on 2022-12-12 01:26

import courses.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=courses.models.chapter_directory_path)),
                ('video_chapter', models.FileField(blank=True, null=True, upload_to=courses.models.chapter_directory_path)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique=True, unique_for_date='published')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=courses.models.user_thumbnail_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=courses.models.user_thumbnail_directory_path)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('authors', models.ManyToManyField(to='courses.author')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=courses.models.lesson_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=courses.models.lesson_directory_path)),
                ('content', models.TextField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.chapter')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
