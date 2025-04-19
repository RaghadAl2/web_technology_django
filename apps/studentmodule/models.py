from django.db import models

# Create your models here.
class Card(models.Model):
    card_number =models.IntegerField()
    
class Department(models.Model):
    name = models.CharField(max_length = 100)
  
class Course(models.Model):
    title = models.CharField(max_length = 100)
    code = models.IntegerField(0)

class Student(models.Model):
    name = models.CharField(max_length = 50)
    card =  models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)