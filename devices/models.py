from django.db import models
from django.core.validators import ValidationError, MinLengthValidator
"""Abstracts"""


class DisplayName(models.Model):
    name = models.SlugField(max_length=45, validators=[MinLengthValidator(1)])

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


class Organization(TimingData, DisplayName):
    # this is a placeholder
    pass


class Network(TimingData, DisplayName):
    owner = models.ForeignKey(Organization)

    def validate_unique(self, *args, **kwargs):
        super(Network, self).validate_unique(*args, **kwargs)

        old_network = self.__class__.objects.filter(
            name=self.name, owner=self.owner.pk)

        if old_network.exists():
            raise ValidationError("Network with that name already exists")


class Node(TimingData, DisplayName):
    network = models.ForeignKey(Network)


class SensorType(TimingData, DisplayName):
    manufacturer = models.CharField(max_length=45)
    units = models.CharField(max_length=10)


class Sensor(TimingData, DisplayName):
    node = models.ForeignKey(Node)
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
