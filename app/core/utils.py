import unicodedata
from typing import Dict, List

from app.tenants.models import Tenant
from django.conf import settings
from django.core import signing
from django.core.cache import cache
from django.utils.crypto import get_random_string
from tenant_schemas.utils import get_tenant_model


def generate_api_key():
    key = get_random_string(length=40)
    return key

def get_tenant(key):
    tenant = cache.get(key)
    if not tenant:
        try:
            tenant = Tenant.objects.get(api_key__key=key)
            cache.set(key, tenant, 300)
        except Tenant.DoesNotExist:
            tenant = None
    return tenant
