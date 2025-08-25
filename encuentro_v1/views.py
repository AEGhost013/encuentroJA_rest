from django.shortcuts import render
from django.http import HttpResponse

#viewsets
from django.contrib.auth import 
from rest_framework import viewsets
# Create your views here.

def prueba(request):
    return HttpResponse('hola mundo')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.