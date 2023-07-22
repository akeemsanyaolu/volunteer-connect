from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    #path('', views.home, name='home')
    path('login/', CustomLoginView, name='login')
]