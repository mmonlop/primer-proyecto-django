from django.db import models


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor',on_delete=models.CASCADE,related_name='posts')
    cuerpo = models.TextField()
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE,related_name='posts') #null=True blank=tue

    def __str__(self):
        return f"{self.titulo}, {self.autor}"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=200)
    email = models.CharField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Categoria(models.Model):
    nombre = models.CharField()

    def __str__(self):
        return f"{self.nombre}"