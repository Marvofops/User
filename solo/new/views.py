from django.shortcuts import render, redirect
from .models import Student, Teacher
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer, TeacherSerializer
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')
class TestView(APIView):
  def get(self, request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
    
  def post(self, request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
    
    
class TeacherView(APIView): 
  def get(self, request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)
    
  def post(self, request):
    serializer = TeacherSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password2 == password:
      if User.objects.filter(username = username).exists():
        return messages.info(request, 'Username already exists')
        return render(request, 'register.html')
      elif User.objects.filter(email=email).exists():
        return messages.info(request, 'Email already exists')
        return render(request,'register.html')
      else:
        User.objects.create_user(username=username,password=password,email=email)
        return redirect('login')
    else:
      return messages.info(request, 'Passwords dont match')
      return render(request,'register.html')
  else:
    return render(request, 'register.html')
    
    
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password= password)
    if user is not None:
      auth.login(request, user)
      return redirect('index')
    else:
      return messages.info(request, 'Invalid credentials')
      return render(request,'login.html')
  else:
    return render(request, 'login.html')
    
    
