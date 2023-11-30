from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Item
from .serializers import ItemSerializer
from django.shortcuts import render
from inventory.models import Item, Product, Warehouse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        item.status = "Fulfilled"
        while item.prev.status != "Fulfilled":
            item.prev.status = "Fulfilled"
            item.prev.save()
        item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data)
