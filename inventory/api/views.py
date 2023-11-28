from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from ..models import Item
from .serializers import ItemSerializer
from django.shortcuts import render
from inventory.models import Item, Product, Warehouse

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer