# Generated by Django 4.1.4 on 2023-01-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_embebe_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='id_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='id_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]