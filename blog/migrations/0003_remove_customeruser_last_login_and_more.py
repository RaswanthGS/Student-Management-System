# Generated by Django 4.1 on 2022-09-06 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_notificationstudent_notificationstaffs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='password',
        ),
    ]