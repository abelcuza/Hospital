from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()
    ci = models.CharField(max_length=11, primary_key=True)
    categoria = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=11, blank=True, null=True)
    imagen = models.ImageField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()
    ci = models.CharField(max_length=11, primary_key=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Medicamento(models.Model):
    tipos_de_medicamentos = [
        ('analgesico', 'Analgésico'),
        ('antiinflamatorio', 'Antiinflamatorio'),
        ('antiacido', 'Antiácido'),
        ('antipirético', 'Antipirético'),
        ('antiinfeccioso', 'Antiinfeccioso'),
        ('antitusivo_mucolitico', 'Antitusivo y mucolítico'),
        ('antialergico', 'Antialérgico'),
        ('antidiarreico_laxante', 'Antidiarreico y Laxante'),
    ]
    nombre_generico = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=tipos_de_medicamentos)

    def __str__(self):
        return self.nombre_generico


class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.RESTRICT)
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT)
    fecha = models.DateTimeField()
    medicamentos = models.ForeignKey(Medicamento, on_delete=models.DO_NOTHING)
    diagnostico = models.TextField(blank=True)


class MedicamentoInventario(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.medicamento
