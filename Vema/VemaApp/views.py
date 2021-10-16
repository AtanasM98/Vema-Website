from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def clients(request):
    return render(request, 'clients.html')


def networks(request):
    return render(request, 'networks.html')


def el_control(request):
    return render(request, 'el_control.html')


def pump_inst(request):
    return render(request, 'pump_inst.html')


def consult(request):
    return render(request, 'consult.html')


def contacts(request):
    return render(request, 'contact.html')
