from django.shortcuts import render
from  .models import User
from .serializers import UsersSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class SignupUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]
    
def userData(request,id):
    users = User.objects.get(id=id)
    serializer = UsersSerializer(users)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData, content_type='application/json')

