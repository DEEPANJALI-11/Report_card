from django.contrib import admin
from .models import *

# Register your models here.
# admin.py
# from django.contrib import admin
# from .models import Student

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'student_id')

# admin.site.register( StudentAdmin)

admin.site.register(hlo)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)


# for displaying all the marks along with student name in admin portl
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,SubjectMarksAdmin)
