from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('contacts', views.contacts, name='contacts'),
    path('el_control', views.el_control, name='el_control'),
    path('networks', views.networks, name='networks'),
    path('pump_inst', views.pump_inst, name='pump_inst'),
    path('consult', views.consult, name='consult'),
]
