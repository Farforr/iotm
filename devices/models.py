from django.db import models

class Network(models.Model):
	name = models.CharField(max_length=45)

class Node(models.Model):
	name = models.CharField(max_length=45)
	network = models.ForeignKey(Network)

class SensorType(models.Model):
	name = models.CharField(max_length=45)
	manufacturer = models.CharField(max_length=45)
	units = models.CharField(max_length=10)

class Sensor(models.Model):
	node  = models.ForeignKey(Node)
	model = models.ForeignKey(SensorType)

class ActuatorType(models.Model):
	name = models.CharField(max_length=45)
	manufacturer = models.CharField(max_length=45)

class Actuator(models.Model):
	node = models.ForeignKey(Node)
	model = models.ForeignKey(ActuatorType)

class SensorData(models.Model):
	value = models.IntegerField()
	sensor = models.ForeignKey(Sensor)
	

