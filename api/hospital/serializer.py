from rest_framework import serializers

from .models import Medico, Paciente, Medicamento, Consulta, MedicamentoInventario


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class ConsultaReadSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    paciente = PacienteSerializer()
    medicamentos = MedicamentoSerializer(many=True)
    fields = ['id', 'medico', 'paciente', 'fecha', 'medicamentos', 'diagnostico']

    class Meta:
        model = Consulta
        fields = '__all__'


class ConsultaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'fecha', 'medicamentos', 'diagnostico']


class MedicamentoReadInventarioSerializer(serializers.ModelSerializer):
    medicamento = MedicamentoSerializer()

    class Meta:
        model = MedicamentoInventario
        fields = ['id', 'medicamento', 'cantidad']


class MedicamentoWriteInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentoInventario
        fields = ['medicamento', 'cantidad']
