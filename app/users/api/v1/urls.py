from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PostsViewSets, UserRegisterView

app_name = "users_api_v1"

router = DefaultRouter()
router.register(r"posts", PostsViewSets)


urlpatterns = [
    path("registration/", UserRegisterView.as_view(), name="registration"),
    path("jwt/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
