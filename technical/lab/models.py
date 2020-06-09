from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PersonaTipos(models.IntegerChoices):
    FISICA = 1
    JURIDICA = 2


# Create your models here.
class Titular(models.Model):
    cuit = models.IntegerField(verbose_name=_("CUIT"), unique=True)
    tipo = models.IntegerField(choices=PersonaTipos.choices)

    def tiene_datos(self):
        return (PersonaFisica.objects.filter(titular=self).exists() or
                PersonaJuridica.objects.filter(titular=self).exists())


class PersonaFisica(models.Model):
    nombre = models.CharField(verbose_name=_("nombre"), max_length=80)
    apellido = models.CharField(verbose_name=_("apellido"), max_length=250)
    dni = models.IntegerField(verbose_name=_("DNI"))
    titular = models.OneToOneField(Titular, related_name='persona_fisica',
                                   on_delete=models.CASCADE, primary_key=True)


def validate_anio(value):
    if value > datetime.now().year:
        raise ValidationError(
            _('%(actual)s es mayor al año actual'),
            params={'actual': value})


class PersonaJuridica(models.Model):
    razon_social = models.CharField(verbose_name=_("razon social"), max_length=100, blank=False)
    anio_fundacion = models.IntegerField(verbose_name=_("anio de fundacion"),
                                         validators=[validate_anio])
    titular = models.OneToOneField(Titular, related_name='persona_juridica',
                                   on_delete=models.CASCADE, primary_key=True)
