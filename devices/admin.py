from django.contrib import admin

from .models import Network, Node, SensorType, ActuatorType, Sensor, Actuator, SensorData, ActuatorData

admin.site.register(Network)
admin.site.register(Node)
admin.site.register(SensorType)
admin.site.register(ActuatorType)
admin.site.register(Actuator)
admin.site.register(SensorData)
admin.site.register(ActuatorData)
