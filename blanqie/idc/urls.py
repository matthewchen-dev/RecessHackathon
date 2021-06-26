from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('learn/', views.learn),
    path('test/', views.test),
]