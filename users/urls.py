from django.urls import path
from  .views import userData
app_name = 'users'


urlpatterns = [
    path('userData/', userData, name='userData'),
]