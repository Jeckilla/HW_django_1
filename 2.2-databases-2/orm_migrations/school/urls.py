from django.urls import path

from school.views import students_list

urlpatterns = [
    path('school/students_list', students_list, name='students'),
]
