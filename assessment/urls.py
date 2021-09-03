from app.users.views import hello
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hi')
]

# API URLS
urlpatterns += [
    # API base url
    path("api/v1/", include("api.v1.urls", namespace="api_v1")),
]

# Swagger
# urlpatterns += [
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
# ]

# # apis for internal use
# internal_schema_view = get_schema_view(
#     openapi.Info(
#         title="OTA API",
#         default_version='v1',
#         description="List of endpoints of Online Travel Nepal.",
#         terms_of_service="",
#         contact=openapi.Contact(email="contact@uddum.com"),
#     ),
#     public=True,
#     # permission_classes=(permissions.IsAuthenticated,),
#     patterns=[path('hello/', hello, name='hi')]
# )

# urlpatterns += [
#     path(
#         '',
#         internal_schema_view.with_ui('swagger', cache_timeout=0),
#         name='internal_swagger_ui',
#     )
# ]
