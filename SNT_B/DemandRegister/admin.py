from django.contrib import admin
from .models import DemandForm,Complaint
# Register your models here.

class AdminDemand(admin.ModelAdmin):
    list_display=[
        'product',
        'number',
        'quantity',
        'consignee_name',
        'consignee_officer',
        'consignee_code',
        'demand_code',
        'allocation_number',
        'accounts_unit',
        'status',
        'declained_reason',
    ]
admin.site.register(Complaint)
admin.site.register(DemandForm,AdminDemand)