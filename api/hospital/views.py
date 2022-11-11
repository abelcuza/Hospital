from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets

from .models import Medico, Paciente, Medicamento, Consulta, MedicamentoInventario
from .serializer import MedicoSerializer, PacienteSerializer, MedicamentoSerializer, ConsultaReadSerializer, \
    ConsultaWriteSerializer, MedicamentoReadInventarioSerializer, MedicamentoWriteInventarioSerializer


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
    filterset_fields = ['nombre', 'apellidos']
    search_fields = ['nombre', 'apellidos']


class PacienteViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class MedicamentoViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class ConsultaViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Consulta.objects.all()

    def get_serializer_class(self):
        return assign_serializer(self, ConsultaReadSerializer, ConsultaReadSerializer,
                                 ConsultaWriteSerializer)


class MedicamentoInventarioViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = MedicamentoInventario.objects.all()

    def get_serializer_class(self):
        return assign_serializer(self, MedicamentoReadInventarioSerializer, MedicamentoReadInventarioSerializer,
                                 MedicamentoWriteInventarioSerializer)
