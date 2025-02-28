from rest_framework import pagination


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'working_days'
    max_page_size = 100
