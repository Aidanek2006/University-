from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserProfileCreateAPIView.as_view(), name='user'),

    path('faculty/', FacultyListAPIView.as_view(), name='faculty'),
    path('faculty/', FacultyCreateAPIView.as_view(), name='faculty'),

    path('teacher/', TeacherListAPIView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher'),

    path('student/', StudentListAPIView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student'),

    path('course/', TeacherListAPIView.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course'),

    path('cabinet/', CabinetViewSet.as_view({'get': 'list'}), name='cabinet'),
    path('schedule/', ScheduleViewSet.as_view({'get': 'list'}), name='schedule'),
    path('recording/', RecordingViewSet.as_view({'get': 'list', 'post': 'create'}), name='recording'),
    path('home_work/', HomeWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='home_work'),
    path('handing_home_work/', HandingHomeWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='handing_home_work'),

]