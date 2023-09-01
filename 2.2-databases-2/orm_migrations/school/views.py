from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers').order_by('st_group')
    print(students)

    return render(request, template, context = {'object_list': students})
