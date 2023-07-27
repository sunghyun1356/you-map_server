from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)

class Purpose(models.Model):
    name = models.CharField(max_length=20)
    
class BuildingPurpose(models.Model):
    building = models.ForeignKey(to ='Building', on_delete=models.CASCADE)
    purpose = models.ForeignKey(to ='Purpose', on_delete=models.CASCADE)
    
class Location(models.Model):
    building = models.ForeignKey(to ='Building', on_delete=models.CASCADE)
    floor = models.IntegerField(null = True, default = 0)