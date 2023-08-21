from rest_framework import serializers
from .models import *

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
class BuildingSerializer(serializers.ModelSerializer):
    purposes= serializers.SerializerMethodField()
    locations = serializers.StringRelatedField(many=True)
    class Meta:
        model = Building
        fields = ['id', 'name', 'nickname', 'latitude', 'longitude', 'purposes', 'locations']

    def get_purposes_queryset(self, building):
        purposes= BuildingPurpose.objects.filter(building=building).select_related("building")
        return purposes
    def get_purposes(self, building):
        queryset = self.get_purposes_queryset(building)
        res = []
        for query in queryset:
            res.append(query.purpose)
        return PurposeSerializer(res, many=True).data


    

