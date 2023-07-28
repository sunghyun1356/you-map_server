from django.contrib import admin
from .models import Building, BuildingPurpose, Purpose, Location

admin.site.register(BuildingPurpose)
admin.site.register(Building)
admin.site.register(Purpose)
admin.site.register(Location)