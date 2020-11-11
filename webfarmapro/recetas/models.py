from django.db import models

class Receta(models.Model):
    NombrePaciente = models.CharField(max_length=50, verbose_name="Nombre del Paciente")
    RutPaciente = models.CharField(max_length=20, verbose_name="Rut Paciente")
    NombreMedicamento = models.CharField(max_length=20, verbose_name="Nombre del Medicamento")
    Dosis = models.IntegerField(verbose_name="Dosis del medicamento en gramos")
    Motivo = models.TextField(verbose_name="Motivo Prescripcion")
    Creacion = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Receta")
    Estado = models.BooleanField(verbose_name="Esta Activa?", default=True)
    Firma = models.FileField(verbose_name="Archivo Firma Electronica")

    def __str__(self):
        return self.NombrePaciente + " " + self.RutPaciente

