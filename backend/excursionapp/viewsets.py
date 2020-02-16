from rest_framework import viewsets
from . import models
from . import serializers


class ExcursionViewset(viewsets.ModelViewSet):
    queryset = models.Excursion.objects.all()
    serializer_class = serializers.ExcursionSerializer
