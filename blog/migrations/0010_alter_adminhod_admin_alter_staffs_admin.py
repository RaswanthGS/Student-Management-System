# Generated by Django 4.1 on 2022-10-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_students_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminhod',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customeruser'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customeruser'),
        ),
    ]