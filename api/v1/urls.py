from django.urls import include, path

app_name = "api_v1"

urlpatterns = [path("users/", include("app.users.api.v1.urls", namespace="users"))]
