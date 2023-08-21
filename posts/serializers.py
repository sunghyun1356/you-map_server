from rest_framework import serializers, pagination

from .models import Post, Comment

from buildings.models import Location, Purpose
from accounts.serializers import UserPreviewSerializer, UserRegisterSerializer

class PostPreviewSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'location', 'image']

class BasePurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ['name', 'glyph', 'posts']

class BuildingPurposeSerializer(BasePurposeSerializer):
    posts = serializers.SerializerMethodField()

    def get_posts_queryset(self, building_id, purpose):
        locations = Location.objects.filter(building_id=building_id)
        posts = Post.objects.filter(purpose=purpose, location__in=locations)

        return posts

    def get_posts(self, purpose):
        building_id = self.context['building_id']
        queryset = self.get_posts_queryset(building_id, purpose)

        return PostPreviewSerializer(queryset, many=True).data

class LimitMixin:
    def limit(self, queryset):
        limit = int(self.context['limit'])
        if (limit <= 0): 
            return queryset
        return queryset[:limit]

class PopularFirstBuildingPurposeSerializer(LimitMixin, BuildingPurposeSerializer):
    def get_posts_queryset(self, building_id, purpose):
        queryset = super().get_posts_queryset(building_id, purpose).order_by('-likes')
        return self.limit(queryset)

class RecentFirstBuildingPurposeSerializer(LimitMixin, BuildingPurposeSerializer):
    def get_posts_queryset(self, building_id, purpose):
        queryset = super().get_posts_queryset(building_id, purpose).order_by('-created_at')
        return self.limit(queryset)
    
# post 상세 조회
class PostDetailSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    writer = UserPreviewSerializer()

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1

    
# post 생성, 수정, 삭제 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'purpose', 'location', 'image']



class PostListSerializer(BasePurposeSerializer):
    posts = serializers.SerializerMethodField()
    def get_posts_queryset(self, purpose):
        posts = Post.objects.filter(purpose=purpose)
        return posts
    def get_posts(self, purpose):
        queryset = self.get_posts_queryset(purpose).order_by('-created_at')
        return PostPreviewSerializer(queryset, many=True).data
    
#purpose별 post 목록