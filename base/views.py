from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields= '__all__'
    

def home(request):
    return HttpResponse('To do list')