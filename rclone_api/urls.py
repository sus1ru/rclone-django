from django.urls import path
from rclone_api import views

urlpatterns = [
  path('hello_view/', views.HelloApiView.as_view()),
]