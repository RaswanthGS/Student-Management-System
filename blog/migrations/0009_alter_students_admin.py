# Generated by Django 4.1 on 2022-10-17 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customeruser'),
        ),
    ]
