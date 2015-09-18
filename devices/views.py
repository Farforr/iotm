from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Network, Node, Organization
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


def index(request):
    error = ''
    if (request.POST and 'new_network_name' in request.POST):
        new_network_name = request.POST['new_network_name']

        network = Network()
        network.name = new_network_name

        # TODO: add a real organization getter
        network.owner = Organization.objects.get()

        # if validation errors, don't save, render the same page but send
        # the errors to the template
        try:
            network.full_clean()
        except ValidationError as e:
            error = e
        else:
            network.save()
            return HttpResponseRedirect(reverse('devices:index'))

    network_list = Network.objects.order_by()

    context = {
        'network_list': network_list,
        'error': error
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
