from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_role = models.CharField(max_length=18, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Faculty(models.Model):#Факультет
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)#факультет
    title = models.CharField(max_length=100) #профессор
    bio = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.department}'


class Student(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.OneToOneField(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.department}'


class Course(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ManyToManyField(Teacher)

    def __str__(self):
        return f'{self.name} - {self.department}'


class Cabinet(models.Model):
    room_number = models.CharField(max_length=16)
    building = models.PositiveSmallIntegerField()#этаж
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_number


class Schedule(models.Model):#Рoсписание
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    DAY_OF_WEEK_CHOICES = (
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    )
    day_of_week = MultiSelectField(max_choices=7, choices=DAY_OF_WEEK_CHOICES)

    def __str__(self):
        return f'{self.course} - {self.classroom}'


class Recording(models.Model):#Запись на курс
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    RECORDING_GRADE_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    grade = models.CharField(max_length=16, choices=RECORDING_GRADE_CHOICES)

    def __str__(self):
        return f'{self.student} - {self.course}'


class HomeWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.course}"


class HandingHomeWork(models.Model):#сдача домашнее задание
    assignment = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    GRADE_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    grade = models.CharField(max_length=16, choices=GRADE_CHOICES)
    feedback = models.TextField()

    def __str__(self):
        return f'{self.assignment} - {self.student}'

