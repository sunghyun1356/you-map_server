from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    latitude = models.IntegerField(default = 0)
    longitude = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=20)
    glyph = models.ImageField(blank = True, upload_to='buildings/purpose')
    
    def __str__(self):
        return self.name
    
class BuildingPurpose(models.Model):
    building = models.ForeignKey(to ='Building', on_delete=models.CASCADE)
    purpose = models.ForeignKey(to ='Purpose', related_name='purposes', on_delete=models.CASCADE)

class Location(models.Model):
    building = models.ForeignKey(to ='Building', related_name='locations', on_delete=models.CASCADE)
    floor = models.IntegerField(default = 0)
    
    def __str__(self):
        building_name = str(self.building)
        floor_representation = ("지하" + str(-self.floor)) if self.floor < 0 else (self.floor)
        return f'{building_name} {floor_representation}층'