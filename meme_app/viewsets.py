from rest_framework import viewsets

from . import models, serializers


class memesViewset(viewsets.ModelViewSet):
    queryset = models.memes.objects.all()
    serializer_class = serializers.memesSerializer
