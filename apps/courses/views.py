from django.shortcuts import render, HttpResponse, redirect
from .models import Course
import datetime

def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name = request.POST['course_name'], description = request.POST['description'])
    return redirect ('/')

def confirm(request, id):
    course = Course.objects.get(id=id)
    context = {
    'courses': course
    }
    return render(request, 'courses/remove.html', context)

def remove(request, id):
    Course.objects.filter(id=id).delete()
    return redirect ('/')
