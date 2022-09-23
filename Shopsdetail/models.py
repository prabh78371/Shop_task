from unicodedata import category
from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=20)
    address  = models.TextField()


class Shopgroup(models.Model):
    shop = models.ForeignKey(Shop,related_name="grp",on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Categories(models.Model):
    group = models.ForeignKey(Shopgroup,related_name="category",on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Subcategories(models.Model):
    category = models.ForeignKey(Categories,related_name="sub_category",on_delete=models.CASCADE)
    name = models.CharField(max_length=20)