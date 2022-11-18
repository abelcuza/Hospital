from django.db import models


class Person(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()
    ci = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=11, blank=True, null=True, unique=True)
    municipio = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Medico(Person):
    especialidades = [
        ('mgi', 'Medico General Integral'),
        ('ginecologo', 'Ginecologo'),
        ('geriatra', 'Geriatra'),
        ('pediatra', 'Pediatra'),
        ('imagenologo', 'Imagenólogo')
    ]
    grados_academicos = [
        ('universitario', 'Universitario'),
        ('master', 'Master en Ciencias'),
        ('doctor', 'Doctor en Ciencias')
    ]

    grado_academico = models.CharField(max_length=100, default='universitario', choices=grados_academicos)
    especialidad = models.CharField(max_length=100, choices=especialidades, default='mgi')

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Paciente(Person):

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
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre_comercial


class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(null=True)
    medicamentos = models.ManyToManyField(Medicamento)
    diagnostico = models.TextField(blank=True)
    tipo_consulta = models.CharField(max_length=100, null=True, blank=True)


class Inventario(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.medicamento
