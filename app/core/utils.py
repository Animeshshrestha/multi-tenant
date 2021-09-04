from django.conf import settings
from django.core.cache import cache
from django.utils.crypto import get_random_string

from app.tenants.models import Tenant


def generate_api_key():
    """
    Generates random api key of length 40
    """
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
