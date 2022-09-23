from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from unicodedata import category
from .models import Shop,Subcategories,Categories,Shopgroup
from rest_framework import serializers

class Subcategoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['category','name']
        depth = 0

class Categoryserilizer(serializers.ModelSerializer):      
    sub_category = Subcategoryserilizer(many=True)
    class Meta:
        model = Categories
        fields = ['group','name','sub_category']
        depth = 0


class Groupserilizer(serializers.ModelSerializer):   
    category = Categoryserilizer(many=True)
    class Meta:
        model = Shopgroup
        fields = ['shop',"name",'category']  
        


class Shopserilizer(serializers.ModelSerializer):
    grp = Groupserilizer(many=True)
    class Meta:
        model = Shop
        fields = ['name','address','grp']
        depth = 0

class Categoryserilizer(serializers.ModelSerializer):   
    
    class Meta:
        model = Categories
        fields = "__all__"
        depth = 0

