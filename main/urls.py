from django.urls import path
from . import views
from .api import RegisterApi

urlpatterns = [
    path('', views.main, name='main'),
    path('api/register/', RegisterApi.as_view()),
    path('generate_url/', views.generate_url, name='generate_url'),
    path('viewpage/', views.viewpage, name='viewpage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
