from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('learn/', views.learn),
    path('test/', views.test),
    path('test/upload/', views.file_upload_view)
]