from django.db import models

"""Abstracts"""
class DisplayName(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True 

class TimingData(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField('last modified', auto_now=True)

    class Meta:
        abstract = True
"""End Abstracts"""

class Network(TimingData, DisplayName):
    pass
    
class Node(TimingData, DisplayName):
    network = models.ForeignKey(Network)

class SensorType(TimingData, DisplayName):
    manufacturer = models.CharField(max_length=45)
    units = models.CharField(max_length=10)

class Sensor(TimingData, DisplayName):
    node  = models.ForeignKey(Node)
    model = models.ForeignKey(SensorType)

class ActuatorType(TimingData, DisplayName):
    manufacturer = models.CharField(max_length=45)

class Actuator(TimingData, DisplayName):
    node = models.ForeignKey(Node)
    model = models.ForeignKey(ActuatorType)

class SensorData(TimingData):
    value = models.IntegerField()
    sensor = models.ForeignKey(Sensor)

class ActuatorData(TimingData):
    value = models.IntegerField()
    actuator = models.ForeignKey(Actuator)
