from app.core.utils import get_tenant
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from tenant_schemas.middleware import DefaultTenantMiddleware
from tenant_schemas.utils import get_public_schema_name


class HTTPHeaderTenantMiddleware(DefaultTenantMiddleware):
    DEFAULT_SCHEMA_NAME = None

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.
        connection.set_schema_to_public()
        key = request.META.get('HTTP_API_KEY')
        if key:
            msg = {'detail': 'Wrong api key provided.'}
            tenant = get_tenant(key)
            if not tenant:
                # Using JsonResponse because rest_framework.exceptions.PermissionDenied
                # is giving 500 error and django.core.exceptions.PermissionDenied is
                # giving sending response.
                return JsonResponse(msg, status=403)
        else:
            return JsonResponse(
                {'detail': 'Api key was not present in HTTP Header.'}, status=403
            )

        request.tenant = tenant
        # for legacy purpose
        request.agency = tenant
        connection.set_tenant(request.tenant)

        # Do we have a public-specific urlconf?
        if (
            hasattr(settings, "PUBLIC_SCHEMA_URLCONF")
            and request.tenant.schema_name == get_public_schema_name()
        ):
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
