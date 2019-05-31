from rest_framework import viewsets
from api.models import Organization
from api.serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Organization
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
