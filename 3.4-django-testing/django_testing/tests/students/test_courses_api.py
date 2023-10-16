import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course():
    return Course.objects.create('C++ для начинающих')

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, make_m2m=True, *args, **kwargs)

    return factory

@pytest.fixture
def course_factory():
    def factory_course(*args, **kwargs):
        students_set = baker.prepare(Student, _quantity=6)
        return baker.make(Course, students=students_set, *args, **kwargs)

    return factory_course


@pytest.mark.django_db
def test_courses(client, course_factory):
    courses = course_factory(_quantity=3)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name



# @pytest.mark.django_db
# def test_courses_id(client, course_factory):
#
#     response = client.get('api/v1/courses/')
#     assert response.status_code == 200

