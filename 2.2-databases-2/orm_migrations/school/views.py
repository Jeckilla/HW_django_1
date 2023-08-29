from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'st_group'
    students = Student.objects.all().order_by(ordering)
    print(students)

    return render(request, template, context = {'object_list': students})
