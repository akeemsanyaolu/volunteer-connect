from django.urls import path
from .views import CustomLoginView, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login')
]