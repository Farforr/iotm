from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Network, Node
from django.core.urlresolvers import reverse


def index(request):
    error_message = ''
    if (request.POST and 'new_network_name' in request.POST):
        new_network_name = request.POST['new_network_name']
        if (new_network_name != ""):
            network = Network()
            network.name = new_network_name
            network.save()
            return HttpResponseRedirect(reverse('devices:index'))
        else:
            error_message = "Please input a name for the new network."

    network_list = Network.objects.order_by()
    context = {
        'network_list': network_list,
        'error_message': error_message
    }

    return render(request, 'devices/index.html', context)


def network_details(request, network_name):
    network = get_object_or_404(Network, name=network_name)

    return render(
        request,
        'devices/network_details.html',
        {'network': network}
    )


def node_details(request, network_name, node_name):
    node = get_object_or_404(Node, name=node_name)
    return render(request, 'devices/node_details.html', {'node': node})
