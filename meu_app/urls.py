from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, OnibusViewSet, LocalizacaoOnibusViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'onibus', OnibusViewSet)
router.register(r'localizacao_onibus', LocalizacaoOnibusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]