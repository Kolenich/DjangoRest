from rest_framework import viewsets
from API.models import Organization
from API.serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Organization
    """
    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer
