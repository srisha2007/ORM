from django.db import models


# Create your models here.
class Orderitem(models.Model):
    ordid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    orddate = models.DateField()
    deliveryaddress = models.CharField()
    itemname = models.CharField()
    unitprice = models.FloatField()
    ordqt = models.IntegerField()
    totalamount = models.FloatField()
