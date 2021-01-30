from django.shortcuts import render
from rest_framework import viewsets
from pettify_crm import models, serializers


class CatViewSet(viewsets.ModelViewSet):
    queryset = models.Cat.objects.all()
    serializer_class = serializers.CatSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
