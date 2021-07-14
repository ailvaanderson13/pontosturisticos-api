from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontosTuristicosViewSet
from atracoes.api.viewsets import AtracoesViewSet
from localizacao.api.viewsets import LocalizacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'endereco', LocalizacaoViewSet)
router.register(r'comentarios', ComentarioViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth-token/', views.obtain_auth_token)
]
