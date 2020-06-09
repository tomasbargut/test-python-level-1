from rest_framework import serializers
from django.utils.translation import  ugettext_lazy as _

from technical.lab.models import PersonaJuridica, PersonaFisica, Titular


class TitularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titular
        fields = '__all__'

    def validate_tipo(self, value):
        if self.instance and self.instance.tiene_datos():
            raise serializers.ValidationError(_("El titular ya tiene datos asociados"))
        return value


class PersonaJuridicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = ['razon_social', 'anio_fundacion']

    def create(self, validated_data):
        titular = validated_data.pop('titular')
        return PersonaJuridica.objects.create(titular=titular, **validated_data)


class PersonaFisicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonaFisica
        fields = ['nombre', 'apellido', 'dni']

    def create(self, validated_data):
        titular = validated_data.pop('titular')
        return PersonaFisica.objects.create(titular=titular, **validated_data)
