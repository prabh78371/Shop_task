from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from typing_extensions import Required
from unicodedata import category
from wsgiref import validate
from .models import Shop,Subcategories,Categories,Shopgroup
from rest_framework import serializers

class Subcategoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['category','name']
        depth = 0

class Categoryserilizer(serializers.ModelSerializer):  
    class Meta:
        model = Categories
        fields = ['group','name']
        depth = 0

        


class Groupserilizer(serializers.ModelSerializer):  
    class Meta:
        model = Shopgroup
        fields = ['shop',"name" ]

    
        
class Shopserilizer(serializers.ModelSerializer):

    class Groupserilizer(serializers.ModelSerializer): 

        class Categoryserilizer(serializers.ModelSerializer):    

            class Subcategoryserilizer(serializers.ModelSerializer):
                category= serializers.HiddenField(default=1)
                class Meta:
                    model = Subcategories
                    fields = ['id','category','name']
                    depth = 2

            sub_category = Subcategoryserilizer(many=True)
            group =serializers.HiddenField(default=1)
            class Meta:
                model = Categories
                fields = ['id','group','name','sub_category']
                depth = 2

        category_set = Categoryserilizer(many=True)
        shop = serializers.HiddenField(default=0)
        class Meta:
            model = Shopgroup
            fields = ['id','shop',"name" ,'category_set' ]
            read_only_fields = ["shop"]
            depth = 2

    grp = Groupserilizer(many=True)

    class Meta:
        model = Shop
        fields = ['id','name','address','grp']
        depth = 3


    def create(self,validated_data):
        grp_validate_data = validated_data.pop('grp')
        shop_data = Shop.objects.create(**validated_data)
        for group in grp_validate_data:
            Shopgroup.objects.create(**group,shop=shop_data)
        return shop_data

   






