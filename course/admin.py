from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'dur_weeks', 'created_at', 'updated_at')
    search_fields = ('title', 'desc')
    list_filter = ('trainers',)