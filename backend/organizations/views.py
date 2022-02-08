from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import OrganizationSerializer
from .models import Organization
from .decorators import is_organization_owner, is_particular_organization_owner

# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A viewset for Organization CRUD, access limited only to organization Managers and Superuser.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @is_organization_owner    
    def create(self, request, pk=None, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @is_particular_organization_owner
    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)        
    
    @is_particular_organization_owner
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return Response({
            'message': 'Deleting of Organizations is not supported!'
        }, status=403)
