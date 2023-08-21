from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from .models import Post
from .serializers import PopularFirstBuildingPurposeSerializer, RecentFirstBuildingPurposeSerializer
from .serializers import PostSerializer, PostDetailSerializer, PostListSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.pagination import CursorPagination


from buildings.models import Purpose


class PurposeListView(generics.ListAPIView):
    serializer_class = RecentFirstBuildingPurposeSerializer  # 기본 시리얼라이저

    def get_serializer_class(self):
        ordering = self.request.query_params.get('ordering', 'recent')  # 기본값 'recent'
        if ordering == 'recent':
            return RecentFirstBuildingPurposeSerializer
        return PopularFirstBuildingPurposeSerializer
    
    def get_queryset(self):
        building_id = self.request.query_params.get('buildingId', None)
        purpose_id = self.request.query_params.get('purposeId', None)
        page_size = self.request.query_params.get('pageSize', 10)  # 기본 페이지 크기 10으로 설정

        if building_id is None:
            raise ValidationError('Missing buildingId query parameter.')
        if page_size is None:
            raise ValidationError('Missing pageSize query parameter.')
        if self.request.query_params.get('ordering') == 'recent' and purpose_id is None:
            raise ValidationError('Missing purposeId query parameter')

        queryset = Purpose.objects.filter(buildingpurpose__building_id=building_id)
        if purpose_id is not None:
            queryset = queryset.filter(id=purpose_id)
        
        return queryset
    
    def get_paginated_response(self, data):
        paginator = CursorPagination()
        paginator.page_size = int(self.request.query_params.get('pageSize', 10))
        return paginator.get_paginated_response(data)

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
