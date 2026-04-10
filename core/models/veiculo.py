from django.db import models

from core.models import Acessorio
from .modelo import Modelo
from .cor import Cor

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank= True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    acessorios = models.ManyToManyField(
        Acessorio,related_name='veiculos', null=True, blank=True)

    def str(self):
        return f"({self.id}) {self.modelo} {self.cor} {self.ano}"

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'