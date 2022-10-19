# Generated by Django 4.1 on 2022-10-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_customeruser_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='user_type',
            field=models.CharField(choices=[('HOD', 'HOD'), ('Staff', 'Staff'), ('Student', 'Student')], default=1, max_length=10),
        ),
    ]