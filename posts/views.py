from django.core.exceptions import ValidationError

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import RecentFirstCursorPagination, PopularFirstCursorPagination

from buildings.models import Location

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PostListAPIViewBase(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)

    def get_queryset(self):
        building_id = self.request.query_params.get('buildingId', None)
        purpose_id = self.request.query_params.get('purposeId', None)
        page_size = self.request.query_params.get('pageSize', None)

        if not (building_id and purpose_id and page_size):
            raise ValidationError("buildingId, purposeId, and pageSize are required query parameters.")

        try:
            page_size = int(page_size)
            if page_size <= 0:
                raise ValidationError("pageSize must be greater than 0.")
        except ValueError:
            raise ValidationError("Invalid value for pageSize.")

        location_ids = Location.objects.filter(building_id=building_id).values_list('id', flat=True)
        queryset = Post.objects.filter(location_id__in=location_ids, purpose_id=purpose_id)

        return queryset

class PopularFirstPostListAPIView(PostListAPIViewBase):
    pagination_class = PopularFirstCursorPagination

class RecentFirstPostListAPIView(PostListAPIViewBase):
    pagination_class = RecentFirstCursorPagination

#post 생성
class PostCreateAPIView(generics.CreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

#post 조회, 수정, 삭제
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return PostDetailSerializer
        return PostSerializer
