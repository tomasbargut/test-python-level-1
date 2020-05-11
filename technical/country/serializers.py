from rest_framework import serializers

from technical.country.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'iso_alpha_code', 'iso_numeric_code']
