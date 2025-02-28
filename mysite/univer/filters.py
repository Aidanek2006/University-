from django_filters import FilterSet
from .models import *


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'department': ['gt', 'lt'],
            'professor': ['gt', 'lt'],

        }

