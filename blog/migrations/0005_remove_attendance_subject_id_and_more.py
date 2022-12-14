# Generated by Django 4.1 on 2022-10-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_customeruser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='subject_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstaffs',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='notificationstaffs',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='students',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='students',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_name',
        ),
        migrations.DeleteModel(
            name='AdminHOD',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CustomerUser',
        ),
        migrations.DeleteModel(
            name='FeedBackStaffs',
        ),
        migrations.DeleteModel(
            name='FeedBackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
        migrations.DeleteModel(
            name='NotificationStaffs',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
        migrations.DeleteModel(
            name='Staffs',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
