from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
