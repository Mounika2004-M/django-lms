from django.contrib import admin
from .models import Batch

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'start_date', 'end_date', 'get_learners', 'trainners']

    def get_learners(self, obj):
        # Display learner names (or you can use username/email instead)
        return ", ".join([user.username for user in obj.learners.all()])

    get_learners.short_description = 'Learners'  # Column title in admin
