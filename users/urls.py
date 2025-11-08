from django.urls import path
from  .views import userData, SignupUser

app_name = 'users'



urlpatterns = [
    path('signup/', SignupUser.as_view(), name='signup'),
    path('userData/<int:id>/', userData, name='userdata'),
]