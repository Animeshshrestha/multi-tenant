from django.db import models
from tenant_schemas.models import TenantMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=16, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    domain_url = None

    # auto_create_schema = True

    def __str__(self):
        return self.schema_name

