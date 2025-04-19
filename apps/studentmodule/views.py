from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, Card, Department, Course
from django.db.models import Q, Count, Min, Max, Sum, Avg , OuterRef, Subquery

# Create your views here.

def lab9_task1(request):
    query =  Department.objects.annotate(student_count=Count('student_module'))

    return render(request, 'studentmodule/show_task1.html',{'query':query})


def lab9_task2(request):
    query =  Course.objects.annotate(student_count=Count('student_module'))
    return render(request, 'studentmodule/show_task2.html',{'query':query})


def lab9_task3(request):
  departments = Department.objects.annotate(oldest_id=Min('id'))
  return render(request, 'studentmodule/show_task3.html',{'departments':departments})



def lab9_task4(request):
    departments = (Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count') )
    return render(request, 'studentmodule/show_task4.html',{'departments':departments})
