from rest_framework import serializers
# from .models import Review
from client.models import Client
from inventory.models import Product
from order.models import Order
from payment.models import Payment
from reviews.models import Reviews



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models =Payment
        fields='__all__'

        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models=Reviews
        fields='__all__'        
      