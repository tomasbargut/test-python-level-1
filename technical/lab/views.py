from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseBadRequest
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.utils.translation import ugettext_lazy as _

from technical.lab import models, serializers
from technical.lab.models import PersonaTipos, PersonaJuridica, PersonaFisica
from technical.lab.serializers import PersonaJuridicaSerializer, PersonaFisicaSerializer


class IsAuthMixin:
    permissions_classes = [permissions.IsAuthenticated]


class TitularViewSet(IsAuthMixin, ModelViewSet):
    queryset = models.Titular.objects.all()
    serializer_class = serializers.TitularSerializer
    titular = None

    def get_titular(self):
        if self.titular is None:
            self.titular = self.get_object()
        return self.titular

    def get_serializer_class(self):
        if self.action in ['datos', 'post_datos', 'put_datos', 'delete_datos']:
            titular = self.get_titular()
            return self._get_serializer_class(titular)

        return super().get_serializer_class()

    @staticmethod
    def _get_serializer_class(titular):
        return (PersonaJuridicaSerializer
                if titular.tipo == PersonaTipos.JURIDICA
                else PersonaFisicaSerializer)

    @staticmethod
    def _get_instance(titular):
        try:
            instance = (titular.persona_fisica
                        if titular.tipo == PersonaTipos.FISICA
                        else titular.persona_juridica)
        except ObjectDoesNotExist:
            raise Http404()
        return instance

    @action(detail=True)
    def datos(self, request, pk=None):
        titular = self.get_titular()
        serializer_class = self._get_serializer_class(titular)
        try:
            instance = self._get_instance(titular)
        except ObjectDoesNotExist:
            raise Http404()

        serializer = serializer_class(instance)
        return Response(serializer.data)

    @datos.mapping.post
    def post_datos(self, request, pk=None):
        titular = self.get_titular()
        if titular.tiene_datos():
            return Response({'detail': _("El titular ya tiene datos asociados")},
                            status.HTTP_400_BAD_REQUEST)

        serializer_class = self._get_serializer_class(titular)
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(titular=titular)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @datos.mapping.put
    def put_datos(self, request, pk=None):
        titular = self.get_titular()
        if not (PersonaFisica.objects.filter(titular=titular).exists() or
                PersonaJuridica.objects.filter(titular=titular).exists()):
            return Response({'detail': _("El titular no tiene datos asociados")},
                            status.HTTP_400_BAD_REQUEST)

        serializer_class = self._get_serializer_class(titular)
        instance = self._get_instance(titular)
        serializer = serializer_class(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @datos.mapping.delete
    def delete_datos(self, request, pk=None):
        titular = self.get_object()
        instance = self._get_instance(titular)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
