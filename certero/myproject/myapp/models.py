from django.db import models

class Proyecto(models.Model):
    TEMA_CHOICES = [
        ('Software', 'Software'),
        ('Matemática', 'Matemática'),
        ('Física', 'Física'),
        # Puedes agregar más opciones según sea necesario
    ]
    
    PATROCINIO_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No'),
    ]
    
    Nombre_Proyecto = models.CharField(max_length=50)
    Estudiante = models.CharField(max_length=50)
    Tema = models.CharField(max_length=50, choices=TEMA_CHOICES)
    Profesor = models.CharField(max_length=50)
    Patrocinio = models.CharField(max_length=2, choices=PATROCINIO_CHOICES, default='No')
    
    def __str__(self):
        return self.Nombre_Proyecto

