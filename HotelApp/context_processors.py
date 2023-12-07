# HotelApp/context_processors.py
from django_tenants.utils import tenant_context, get_tenant_model

def tenant(request):
    tenant = get_tenant_model().objects.get(schema_name=request.tenant.schema_name)
    return {
        'tenant': tenant
    }