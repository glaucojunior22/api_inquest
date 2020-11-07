from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from core.models import Person, Enterprise, Possession


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = Person.objects.all()


class EnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnterpriseSerializer
    queryset = Enterprise.objects.all()


class PossessionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnterpriseSerializer
    queryset = Possession.objects.all()