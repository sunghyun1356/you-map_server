from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Post
from .serializers import PopularFirstBuildingPurposeSerializer, RecentFirstBuildingPurposeSerializer

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