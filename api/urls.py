"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from api.hospital import views as hospital_views

router = routers.DefaultRouter()
router.register(r'medicos', hospital_views.MedicoViewSet, basename='medicos')
router.register(r'pacientes', hospital_views.PacienteViewSet, basename='pacientes')
router.register(r'medicamentos', hospital_views.MedicamentoViewSet, basename='medicamentos')
router.register(r'consultas', hospital_views.ConsultaViewSet, basename='consultas')
router.register(r'inventario', hospital_views.InventarioViewSet, basename='inventario')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', authtoken_views.obtain_auth_token)
]
