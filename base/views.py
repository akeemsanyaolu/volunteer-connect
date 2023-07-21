from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'

def home(request):
    return HttpResponse('To do list')