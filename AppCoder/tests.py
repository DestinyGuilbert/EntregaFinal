import random
import string

from django.test import TestCase
from .models import Profesor


KEY_LEN = 20
keylistNombre = [random.choice((string.ascii_letters + string.digits)) for i in range(KEY_LEN)]
nombrePrueba = "".join(keylistNombre)


class ProfesorModelTest(TestCase):
    def setUp(self):
        self.profesor = Profesor.objects.create(
            nombre=nombrePrueba,
            apellido="Pérez",
            email="juan.perez@example.com",
            profesion="Matemático"
        )

    def test_profesor_fields(self):
        profesor = self.profesor
        self.assertEqual(profesor.nombre, nombrePrueba)
        self.assertEqual(profesor.apellido, "Pérez1")
        self.assertEqual(profesor.email, "juan.perez@example.com")
        self.assertEqual(profesor.profesion, "Matemático")

    def test_profesor_str(self):
        profesor = self.profesor
        expected_str = f"Nombre: {nombrePrueba} - Apellido Pérez - E-Mail juan.perez@example.com"
        self.assertEqual(str(profesor), expected_str)

# Ejecutar: python manage.py test
