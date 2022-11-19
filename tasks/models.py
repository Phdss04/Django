from django.db import models

# Create your models here.
class Task(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(verbose_name="Descrição")
    feito = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome