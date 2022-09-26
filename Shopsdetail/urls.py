from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.shops,name="Shop"),
    path('group/',views.group_info,name="gi"),
    path('cat/',views.cat,name="Shop"),
    path('sub/',views.subcat,name="Shop"),
    path('shop/',views.shops,name="Shop"),
]