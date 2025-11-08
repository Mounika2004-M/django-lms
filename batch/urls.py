from django.urls import path
from . import views
app_name = 'batch'

urlpatterns = [
    path('', views.batch_view, name='batch-list-create'),
]
