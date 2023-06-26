from django.shortcuts import render
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all()
    context = {'resources': resources}
    return render(request, 'resources/resource_list.html', context)

def resource_detail(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    context = {'resource': resource}
    return render(request, 'resources/resource_detail.html', context)
