from rest_framework import serializers

from .models import Medico, Paciente, Medicamento, Consulta, Inventario


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


class MedicamentoConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['nombre_comercial']


class ConsultaReadSerializer(serializers.ModelSerializer):
    medico = serializers.SerializerMethodField()
    paciente = serializers.SerializerMethodField()
    medicamentos = serializers.SerializerMethodField()
    paciente_id = serializers.SerializerMethodField()
    medico_id = serializers.SerializerMethodField()

    # medicamentos = MedicamentoConsultaSerializer(many=True)

    def get_medico(self, obj):
        return obj.medico.__str__()

    def get_paciente(self, obj):
        return obj.paciente.__str__()

    def get_paciente_id(self, obj):
        return obj.paciente.id

    def get_medico_id(self, obj):
        return obj.medico.id

    def get_medicamentos(self, obj):
        return [m.nombre_comercial for m in obj.medicamentos.all()]

    # def get_medicamentos(self):

    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'fecha', 'medicamentos', 'diagnostico', 'medico', 'medico_id', 'paciente_id',
                  'tipo_consulta']


class ConsultaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'fecha', 'medicamentos', 'diagnostico', 'tipo_consulta']


class InventarioReadSerializer(serializers.ModelSerializer):
    medicamento = serializers.SerializerMethodField()

    def get_medicamento(self, obj):
        return obj.medicamento.nombre_comercial

    class Meta:
        model = Inventario
        fields = ['id', 'medicamento', 'cantidad']


class InventarioWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['medicamento', 'cantidad']
