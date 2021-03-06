import re
from datetime import date
from typing import Dict

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from utils.validacpf import valida_cpf

from perfis.choices import Estados


# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        choices=Estados.choices,
        default=Estados.RIO_DE_JANEIRO,
    )

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")

    def __str__(self) -> str:
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    def clean(self) -> None:
        error_message: Dict[str, str] = {}

        if not valida_cpf(self.cpf):
            error_message["cpf"] = "Digite um CPF valido"

        if re.search(r"[^0-9]", self.cep) or len(self.cep) < 8:
            error_message["cep"] - "CEP invalido, digite os 8 digitos do CEP"

        if error_message:
            raise ValidationError(error_message)

    def get_absolute_url(self) -> str:
        return reverse("perfil_detail", kwargs={"pk": self.pk})

    @property
    def idade(self) -> int:
        hoje: date = date.today()
        return (
            hoje.year
            - self.data_nascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.data_nascimento.month, self.data_nascimento.day)
            )
        )
