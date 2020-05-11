from django.utils import timezone

from django.db.models import Model, DateTimeField, IntegerField


class Audit(Model):
    class Meta:
        abstract = True

    create_date = DateTimeField(default=timezone.now, verbose_name='Fecha de creación')
    write_date = DateTimeField(default=timezone.now, verbose_name='Fecha de modificación')
    version = IntegerField(default=1, verbose_name='Versión')
