from rest_framework.serializers import ModelSerializer
from ..models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('prev', 'stock_id', 'status', 'product_id', 'warehouse_id', 'next')
