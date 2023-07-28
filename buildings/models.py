from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=20)
    glyph = models.ImageField(blank = True, upload_to='buildings/purpose')
    
    def __str__(self):
        return self.name
    
class BuildingPurpose(models.Model):
    building = models.ForeignKey(to ='Building', on_delete=models.CASCADE)
    purpose = models.ForeignKey(to ='Purpose', on_delete=models.CASCADE)
    latitude = models.IntegerField(default = 0)
    longitude = models.IntegerField(default = 0)
    
class Location(models.Model):
    building = models.ForeignKey(to ='Building', on_delete=models.CASCADE)
    floor = models.IntegerField(default = 0)
