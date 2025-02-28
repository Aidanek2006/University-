from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import *
from .serializers import *


class UserProfileCreateAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FacultyListAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListSerializer


class FacultyCreateAPIView(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListSerializer


class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['user']


class TeacherDetailAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['user']


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['professor', 'department']
    search_fields = ['name']


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseListSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raice_exception=True)
            course = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({'detail': 'Маалымат туура эмес берилди'}, status.HTTP_400_BAD_REQUEST)
        except NameError as e:
            return Response({'detail': 'Ошибка в коде'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception:
            return Response({'detail': 'Сервер не работает'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer


class HomeWorkViewSet(viewsets.ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer


class HandingHomeWorkViewSet(viewsets.ModelViewSet):
    queryset = HandingHomeWork.objects.all()
    serializer_class = HandingHomeWorkSerializer

