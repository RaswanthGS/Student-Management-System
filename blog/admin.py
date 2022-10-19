from django.contrib import admin
from .models import *

admin.site.register(CustomerUser)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
