from django.db import models

class Familiar(models.Model):
   
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=300)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.nacionalidad}, {self.edad}, {self.id}"

        