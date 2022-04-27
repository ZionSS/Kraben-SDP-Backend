from dataclasses import field
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.views import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':False
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id','user','user_type','first_name','last_name','email','address','district','province','pincode']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','price','img','amount']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','product_id','quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = ['id','items','status']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        moder = Cart
        field = ['user_id','items']