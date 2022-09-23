from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import Shopserilizer,Groupserilizer, Subcategoryserilizer
from .models import Shop,Shopgroup, Subcategories
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def shops(request):
    if request.method ==  'GET':
        prod = Shop.objects.all()
        serilizer = Shopserilizer(prod,many=True)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    if request.method == 'POST':
        serilizer = Shopserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)
