from django.db import models

class Network(models.Model):
	name = models.CharField(max_length=45)

class Node(models.Model):
	name = models.CharField(max_length=45)
	network = models.ForeignKey(Network)

