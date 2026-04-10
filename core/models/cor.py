from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=40)

    def str(self):
        return f"({self.id}) {self.nome}"

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'