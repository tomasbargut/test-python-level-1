from django.db.models import Model, CharField

from technical.audit.models import Audit


class Country(Audit):
    iso_alpha_code = CharField(max_length=2, verbose_name='Código Alfabético ISO')
    iso_numeric_code = CharField(max_length=3, verbose_name='Código Numérico ISO')
    name = CharField(max_length=27, verbose_name='Nombre')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name
