from django.urls import path
from .views import TestView, TeacherView
from . import views

urlpatterns = [
  path('testview/', TestView.as_view(), name = 'test'),
  path('teacherview/', TeacherView.as_view(), name = 'test2'),
  path('register', views.register, name = 'register'),
  path('login', views.login, name = 'login'),
  path('', views.index, name = 'index'),
  
  ]