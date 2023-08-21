from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 100

class RecentFirstCursorPagination(CustomCursorPagination):
    ordering = '-created_at'

class PopularFirstCursorPagination(CustomCursorPagination):
    ordering = '-likes'