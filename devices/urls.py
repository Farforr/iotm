from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^(?P<network_name>[a-zA-Z0-9_ ]+)/$', views.network_details, name='network_details'),
    url(r'^(?P<network_name>[a-zA-Z0-9_ ]+)/(?P<node_name>[a-zA-Z0-9_ ]+)/$', views.node_details, name='node_details'),
    # url(r'^(?<node_id>[0-9]+)/add_sensor/$', views.addSensor, name='add_sensor')
]