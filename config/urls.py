from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from trufas.views import ComboViewSet, SaborViewSet

router = DefaultRouter()
router.register(r"combo", ComboViewSet)
router.register(r"sabor", SaborViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]