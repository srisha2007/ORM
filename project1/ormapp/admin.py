from django.contrib import admin
from .models import Orderitem
admin.site.register(Orderitem);
class OrderitemAdmin(admin.ModelAdmin):
        list_display = ('ordid','userid','orddate','deliveryaddress','itemname','unitprice','ordqt','totalamount')