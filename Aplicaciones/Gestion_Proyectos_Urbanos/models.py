from django.db import models

class Contratista(models.Model):
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    especialidad = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class ProyectoUrbano(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class ZonaVerde(models.Model):
    nombre = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Área en metros cuadrados")
    ubicacion = models.CharField(max_length=255)
    proyecto = models.ForeignKey(ProyectoUrbano, on_delete=models.CASCADE, related_name='zonas_verdes')
    foto = models.ImageField(upload_to='zonas_verdes/', blank=True, null=True)  # Nuevo campo para imágenes

    def __str__(self):
        return self.nombre

class ConstruccionSostenible(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=[('Edificio', 'Edificio'), ('Parque', 'Parque'), ('Infraestructura', 'Infraestructura')])
    materiales_sostenibles = models.TextField()
    eficiencia_energetica = models.BooleanField(default=False)
    proyecto = models.ForeignKey(ProyectoUrbano, on_delete=models.CASCADE, related_name='construcciones_sostenibles')
    
    def __str__(self):
        return self.nombre
