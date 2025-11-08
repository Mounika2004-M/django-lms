from django.urls import path
from .views import course_list_create
app_name = 'course'

urlpatterns = [
    path('', course_list_create, name='course-list-create'),
]