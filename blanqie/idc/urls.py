from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('learn/', views.learn, name="learn"),
    path('test/', views.test, name="test"),
    path('test/upload/', views.file_upload_view),
    path('test/dl/', views.download),
]