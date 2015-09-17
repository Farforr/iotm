from django.shortcuts import render, get_object_or_404

from .models import Network, Node

def index(request):
    network_list = Network.objects.order_by()
    context = {'network_list':network_list}
    return render(request, 'devices/index.html', context)

def network_details(request, network_name):
    network = get_object_or_404(Network, name=network_name)
    return render(request, 'devices/network_details.html', {'network': network})

def node_details(request, network_name, node_name):
    node = get_object_or_404(Node, name=node_name)
    return render(request, 'devices/node_details.html', {'node': node})