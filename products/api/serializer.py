from rest_framework import serializers
from products import models
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
        ]
class EntrepreneurSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)    
    class Meta:
        model = models.Entrepreneur
        fields = [
            'user',
            'address'
        ]

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    entrpr = EntrepreneurSerializer(required=True)
    class Meta:
        model = models.Product
        fields = [
            'id',
            'name',
            'price',
            'img',
            'entrpr',
            'quantity'
        ] 

