from rest_framework.routers import DefaultRouter
from inventory.api.urls import item_router
from django.urls import path, include

router = DefaultRouter()
router.registry.extend(item_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
