from django.contrib import admin
from .models import Student, Grade


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'year', 'group')
    list_filter = ('year',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "score")
    list_filter = ('student',)
