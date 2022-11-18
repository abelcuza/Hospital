from django.test import TestCase

from api.hospital.models import Medico


class MedicoTestCase(TestCase):
    def setUp(self):
        self.medico = Medico.objects.create(
            nombre="Medico",
            apellidos="Test",
            email="medico@test.com",
            ci="999999999",
            direccion="test_direction",
            telefono="+5355555555",
            municipio="test_municipio",
            provincia="test_provincia",
            grado_academico="universitario",
            especialidad="mgi",
        )

    def test_get_medico(self):
        assert Medico.objects.get(apellidos="Test")