from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

item_router = DefaultRouter()
item_router.register('', ItemViewSet, basename='item')
urlpatterns = item_router.urls