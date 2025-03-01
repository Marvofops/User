from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length = 100)
  grade = models.CharField(max_length= 2)
  age = models.CharField(max_length= 2)
  details = models.CharField(max_length=500)
  
  def __str__(self):
    return self.name
    
class Teacher(models.Model):
  name = models.CharField(max_length = 100)
  subject = models.CharField(max_length= 100)
  age = models.CharField(max_length= 2)
  details = models.CharField(max_length=500)
  
  def __str__(self):
    return self.name
    

