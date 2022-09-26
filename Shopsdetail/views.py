from email.headerregistry import Group
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import Categoryserilizer, Shopserilizer,Groupserilizer, Subcategoryserilizer
from .models import Categories, Shop,Shopgroup, Subcategories
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
# Create your views here.

@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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


@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def group_info(request):
    if request.method ==  'GET':
        prod = Shopgroup.objects.all()
        serilizer = Groupserilizer(prod,many=True)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    if request.method == 'POST':
        serilizer = Groupserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def cat(request):
    if request.method ==  'GET':
        prod = Categories.objects.all()
        serilizer = Categoryserilizer(prod,many=True)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    if request.method == 'POST':
        serilizer = Categoryserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def subcat(request):
    if request.method ==  'GET':
        prod = Subcategories.objects.all()
        serilizer = Subcategoryserilizer(prod,many=True)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    if request.method == 'POST':
        serilizer = Subcategoryserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)