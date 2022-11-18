from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Medico, Paciente, Medicamento, Consulta, Inventario
from .serializer import MedicoSerializer, PacienteSerializer, MedicamentoSerializer, ConsultaReadSerializer, \
    ConsultaWriteSerializer, InventarioWriteSerializer, InventarioReadSerializer


def assign_serializer(obj, list_serializer, read_serializer, write_serializer):
    p = {
        'retrieve': read_serializer,
        'update': write_serializer,
        'create': write_serializer,
        'list': list_serializer,
        'partial_update': write_serializer,
    }
    if obj.action in p:
        return p[obj.action]
    return read_serializer


class MedicoViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filterset_fields = ['municipio', 'provincia', 'grado_academico', 'especialidad']
    search_fields = ['^nombre', '^apellidos']

    @action(detail=False, methods=['GET'], name='Get Filters', url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class PacienteViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filterset_fields = ['municipio', 'provincia']
    search_fields = ['^nombre', '^apellidos']

    @action(detail=False, methods=['GET'], name='Get Filters', url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class MedicamentoViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filterset_fields = ['tipo']
    search_fields = ['^nombre_generico', '^nombre_comercial', '^tipo']

    @action(detail=False, methods=['GET'], name='Get Filters', url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class ConsultaViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    filterset_fields = ['medico', 'paciente', 'fecha']
    search_fields = ['^medico', '^paciente']

    @action(detail=False, methods=['GET'], name='Get Filters', url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        return assign_serializer(self, ConsultaReadSerializer, ConsultaReadSerializer,
                                 ConsultaWriteSerializer)


class InventarioViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    filterset_fields = ['medicamento']
    search_fields = ['^medicamento__nombre_comercial']

    def get_serializer_class(self):
        return assign_serializer(self, InventarioReadSerializer, InventarioReadSerializer,
                                 InventarioWriteSerializer)

    @action(detail=False, methods=['GET'], name='Get Filters', url_path='filters')
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)
