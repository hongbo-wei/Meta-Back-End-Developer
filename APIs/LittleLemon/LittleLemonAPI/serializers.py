from .models import Category, MenuItem, Cart, Order, OrderItem
from rest_framework import serializers
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
    

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'feature', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
        }


class CartSerializer(serializers.ModelSerializer):
    # menuitem = MenuItemSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
        extra_kwargs = {
            'quantity': {'min_value': 1},
        }


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order_id', 'menuitem_id', 'quantity', 'unit_price', 'price']
        extra_kwargs = {
            'quantity': {'min_value': 1},
        }


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'orderitems']
        extra_kwargs = {
            'total': {'min_value': 1},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'