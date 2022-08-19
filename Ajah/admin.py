from django.contrib import admin

# Register your models here.
from .models import *


class Course_WorkAdmin(admin.ModelAdmin):
    list_display=('cohort_id','topic','subtopics','date_added')
    list_filter=('cohort_id', 'topic','date_added')

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('cohort_id','names','date_added')
    list_filter=('cohort_id', 'names','date_added')


class GradeAdmin(admin.ModelAdmin):
    list_display=('cohort_id','name', 'serial_number','grade','date_added')
    list_filter=('cohort_id', 'name','date_added')



admin.site.register(Course_Work, Course_WorkAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Grade, GradeAdmin)


