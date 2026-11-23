from rest_framework import serializers
from .models import *
from accounts.serailizers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        read_only_fields = ['orders_count']

    def to_representation(self,instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user','total_price','status','created_at']

    def to_representation(self,instance):
        data = super().to_representation(instance)
        data['dish'] = DishSerializer(instance.dish).data
        data['user'] = UserSerializer(instance.user).data
        return data


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']