# Generated by Django 4.1 on 2022-10-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_adminhod_admin_alter_staffs_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_date',
            field=models.DateField(),
        ),
    ]
