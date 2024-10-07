from rest_framework import serializers
from .models import Usuario, Onibus, LocalizacaoOnibus

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Isso inclui todos os campos do modelo

class OnibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onibus
        fields = '__all__'

class LocalizacaoOnibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacaoOnibus
        fields = '__all__'