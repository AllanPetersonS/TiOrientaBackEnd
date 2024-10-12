from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Onibus, LocalizacaoOnibus
from .serializers import UsuarioSerializer, OnibusSerializer, LocalizacaoOnibusSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class OnibusViewSet(viewsets.ModelViewSet):
    queryset = Onibus.objects.all()
    serializer_class = OnibusSerializer

class LocalizacaoOnibusViewSet(viewsets.ModelViewSet):
    queryset = LocalizacaoOnibus.objects.all()
    serializer_class = LocalizacaoOnibusSerializer