from django.urls import path
from . import views
from dashboard.models import User

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('signup/', views.create_account, name='signup')
]