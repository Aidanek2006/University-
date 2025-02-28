from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'description']


class FacultyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class TeacherListSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'department']


class TeacherDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Student
        fields = ['user', 'department']


class StudentDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    department = FacultyListSerializer()
    class Meta:
        model = Course
        fields = ['name']


class CourseDetailSerializer(serializers.ModelSerializer):
    department = FacultyListSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    classroom = CabinetSerializer()

    class Meta:
        model = Schedule
        fields = '__all__'


class RecordingSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    course = CourseListSerializer()

    class Meta:
        model = Recording
        fields = '__all__'


class HomeWorkSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = HomeWork
        fields = '__all__'


class HandingHomeWorkSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()

    class Meta:
        model = HandingHomeWork
        fields = '__all__'


