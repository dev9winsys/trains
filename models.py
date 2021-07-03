from django.db import models


# Create your models here.
class TrainLine(models.Model):
    trainID = models.CharField(max_length=5)
    trainName = models.CharField(max_length=200)
    trainNameEng = models.CharField(max_length=200)
    trainCompany = models.CharField(max_length=200)
    trainSearch = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.trainName


class StationList(models.Model):
    stationNo = models.CharField(max_length=6)
    trainName = models.CharField(max_length=200)
    stationID = models.CharField(max_length=6)
    stationName = models.CharField(max_length=200)
    stationDistince = models.CharField(max_length=200)
    stationNameEng = models.CharField(max_length=200)

    def __str__(self):
        return '<div id=row><div id=stationID>'+self.stationNo+'</div><div id=stationName>'+self.stationName+'</div><div id=stationNameEng>'+self.stationNameEng+'</div></div>'
