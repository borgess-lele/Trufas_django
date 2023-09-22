from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from trufas.views import ComboViewSet, SaborViewSet, Sem_LactoseViewSet
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"combo", ComboViewSet)
router.register(r"sabor", SaborViewSet)
router.register(r"sem_lactose", Sem_LactoseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)