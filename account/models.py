from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=45)

class User(models.Model):
	name = models.CharField(max_length=45)
	organization = models.ManyToManyField(Organization)
	email = models.EmailField()
