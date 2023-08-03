from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from .models import Post
from .serializers import PopularFirstBuildingPurposeSerializer, RecentFirstBuildingPurposeSerializer
from .serializers import PostSerializer, PostDetailSerializer, PostListSerializer
from .permissions import IsOwnerOrReadOnly

from buildings.models import Purpose


class PurposeListView(generics.ListAPIView):
    def get_serializer_class(self):
        ordering = self.kwargs['ordering']
        if ordering == 'recent':
            return RecentFirstBuildingPurposeSerializer
        
        return PopularFirstBuildingPurposeSerializer
    
    def get_queryset(self):
        building_id = self.request.query_params.get('buildingId', None)
        purpose_id = self.request.query_params.get('purposeId', None)
        limit = self.request.query_params.get('limit', None)

        if building_id is None:
            raise ValidationError('Missing buildingId query parameter.')
        if limit is None:
            raise ValidationError('Missing limit query parameter.')
        if self.kwargs['ordering'] == 'recent' and purpose_id is None:
            raise ValidationError('Missing purposeId query parameter')
        
        purposes = Purpose.objects.filter(buildingpurpose__building_id=building_id)
        if purpose_id is not None:
            purposes = purposes.filter(id=purpose_id)
        
        return purposes
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['building_id'] = self.request.query_params['buildingId']
        context['limit'] = self.request.query_params['limit']
        return context
    
    def get(self, request, *args, **kwargs):
        try: 
            return super().get(request, *args, **kwargs)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

#post 전체 목록
class PostListAPIView(generics.ListAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PostListSerializer

#post 생성
class PostCreateAPIView(generics.CreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

# url 
def postListCreateCombined(request, *args, **kwargs):
    if request.method == 'GET':
        return PostListAPIView.as_view()(request, *args, **kwargs)
    elif request.method == 'POST':
        return PostCreateAPIView.as_view()(request, *args, **kwargs)


#post 조회, 수정, 삭제
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return PostDetailSerializer
        return PostSerializer

# purpose별 최신 posts 목록 - pagination

# 지금 가장 인기 있는 장소