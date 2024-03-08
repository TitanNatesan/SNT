from django.db import models

class DemandForm(models.Model):
    product = models.CharField( max_length=200)
    number = models.BigIntegerField()
    quantity = models.IntegerField()
    nos = models.CharField( max_length=100)
    consignee_name = models.CharField( max_length=100)
    consignee_officer = models.CharField(max_length=100)
    consignee_code = models.CharField(max_length=50)
    demand_code = models.CharField(max_length=50)
    allocation_number = models.CharField( max_length=50)
    accounts_unit = models.CharField( max_length=100)
    date = models.DateTimeField(auto_now_add=True,null=True)
