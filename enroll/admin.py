from django.contrib import admin
from enroll.models import StudentInfo,StudentAcademics

# Register your models here.
admin.site.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_dispaly = ('Name')
admin.site.register(StudentAcademics)
