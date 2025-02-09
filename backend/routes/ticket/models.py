from django.utils import timezone
from django.db import models
from routes.patio.models import Patio

class Ticket(models.Model):
    Veiculo = models.IntegerChoices("Veiculo", "Carro Moto")

    codigo = models.CharField(max_length=6)
    patio_id = models.ForeignKey(Patio, on_delete=models.CASCADE)   
    entrada = models.DateTimeField(default=timezone.now)
    saida = models.DateTimeField(null=True, blank=True)
    veiculo = models.IntegerField(choices=Veiculo.choices, default=1)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    