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
    product = models.OneToOneField("DemandRegister.Product", on_delete=models.CASCADE)
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
    sopt =(
        ("Pending","Pending"),
        ("Declined","Declined"),
        ("Accepted","Accepted"),
    )
    status = models.CharField(max_length=50,choices=sopt,default='Pending')
    declained_reason = models.TextField(null=True)

class Complaint(models.Model):
    consignee_name = models.CharField( max_length=100)
    reference = models.CharField( max_length=100)
    date = models.DateField(auto_now_add=True)
    complaint = models.TextField()
    product = models.OneToOneField("DemandRegister.Product", on_delete=models.CASCADE)
    slnoItem = models.BigIntegerField()
    dom = models.IntegerField() #year of manufactured

    def __str__(self) -> str:
        return f'{self.slnoItem}'

class issued_complaint(models.Model):
    reference = models.CharField( max_length=100)
    consignee_name = models.CharField( max_length=100)
    consignee_officer = models.CharField(max_length=100)
    description  = models.CharField(max_length=100)
    slnoItem = models.BigIntegerField()
    dom = models.IntegerField() #year of manufactured
    make = models.CharField(max_length=100)
    defects_reported = models.TextField()
    
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    plno = models.CharField(max_length=50,null=True)
    
    
    
    
    
'''
  PRODUCT_CHOICES = (
    ('RELAY OT2-2F/2B (9 Ohms)', 'RELAY OT2-2F/2B (9 Ohms)'),
    ('RELAY OBA1-8F/8B', 'RELAY OBA1-8F/8B'),
    ('RELAY QECX-4F/4B', 'RELAY QECX-4F/4B'),
    ('RELAY QNA1K 100 ohms 24V 6F/6B', 'RELAY QNA1K 100 ohms 24V 6F/6B'),
    ('IPS/CHARGER FALURE SM\'S ALERT SYSTEM', 'IPS/CHARGER FALURE SM\'S ALERT SYSTEM'),
    ('TLBI WITH UFSBI', 'TLBI WITH UFSBI'),
    ('IRS POINT MACHINE 220MM STROKE', 'IRS POINT MACHINE 220MM STROKE'),
    ('E-TYPE LOCK', 'E-TYPE LOCK'),
    ('ELECTRIC KEY TRANSMITTER', 'ELECTRIC KEY TRANSMITTER'),
    ('LIFTING BARRIER GATE', 'LIFTING BARRIER GATE'),
    ('FRP ROAD WARNING EQUIPMENT', 'FRP ROAD WARNING EQUIPMENT'),
    ('LC GATE PANEL', 'LC GATE PANEL'),
    ('EMERGENCY PANEL FOR ELECTRONIC INTERLOCKING', 'EMERGENCY PANEL FOR ELECTRONIC INTERLOCKING'),
    ('INDICATION PANEL', 'INDICATION PANEL'),
    ('EMERGENCY SLIDING BOOM BARRIER GATE', 'EMERGENCY SLIDING BOOM BARRIER GATE'),
    ('BOOM FOR LIFTING BARRIER GATE 9.76mtr', 'BOOM FOR LIFTING BARRIER GATE 9.76mtr'),
    ('LED SIGNAL BASED TORCH LIGHT', 'LED SIGNAL BASED TORCH LIGHT'),
    ('GROUND CONNECTION SPECIAL(THREAD) SCREW TYPE FOR ELECTRIC POINT M/C 143MM', 'GROUND CONNECTION SPECIAL(THREAD) SCREW TYPE FOR ELECTRIC POINT M/C 143MM'),
    ('RELAY TEST KIT (CR TEST PANEL)', 'RELAY TEST KIT (CR TEST PANEL)'),
    ('TRACK FEED BATTERY CHARGER', 'TRACK FEED BATTERY CHARGER'),
    ('BATTERY CHARGER MONITORING SYSTEM', 'BATTERY CHARGER MONITORING SYSTEM'),
    ('FTOT FOR 500 TERMINAL', 'FTOT FOR 500 TERMINAL'),
    ('TRAIN SHUNT RESISTANCE METER', 'TRAIN SHUNT RESISTANCE METER'),
    ('ISOLATION TRANSFORMER 110\\110 VOLT AC 50hz & 50 VA', 'ISOLATION TRANSFORMER 110\\110 VOLT AC 50hz & 50 VA'),
    ('GRS APPARATUS CASE FULL SIZE SUITABLE FOR REMOTE TERMINAL UNIT (RTU)', 'GRS APPARATUS CASE FULL SIZE SUITABLE FOR REMOTE TERMINAL UNIT (RTU)'),
    ('GROUND CONNECTION FOR IS POINT MACHINE 220MM STROKE', 'GROUND CONNECTION FOR IS POINT MACHINE 220MM STROKE'),
    ('GALVANISED GROUND CONNECTION FOR IRS POINT MACHINE 143MM STROKE', 'GALVANISED GROUND CONNECTION FOR IRS POINT MACHINE 143MM STROKE'),
    ('DYNAMIC HAND SET WITH PCB FOR TLB/DLBTLEDLE', 'DYNAMIC HAND SET WITH PCB FOR TLB/DLBTLEDLE'),
    ('DIGITAL VOICE ANNOUNCING SYSTEM', 'DIGITAL VOICE ANNOUNCING SYSTEM'),
    ('MAINTAINER HEAD LAMP', 'MAINTAINER HEAD LAMP'),
    ('CONDENSER UNIT IN SET', 'CONDENSER UNIT IN SET'),
    ('SIEMENS RELAY RACK', 'SIEMENS RELAY RACK'),
    ('RS POINT MACHINE 143MM STROKE (400 VOLTE)', 'RS POINT MACHINE 143MM STROKE (400 VOLTE)'),
    ('IRS POINT MACHINE 143MM STROKE (IP 67)', 'IRS POINT MACHINE 143MM STROKE (IP 67)'),
    ('IRS POINT MACHINE 143MM STROKE (IP 67 & 400 VOLTE)', 'IRS POINT MACHINE 143MM STROKE (IP 67 & 400 VOLTE)'),
    ('IRS POINT MACHINE 220MM STROKE (400 VOLTE)', 'IRS POINT MACHINE 220MM STROKE (400 VOLTE)'),
    (' IRS POINT MACHINE 220MM STROKE (IP 67)', ' IRS POINT MACHINE 220MM STROKE (IP 67)'),
    ('IRS POINT MACHINE 220MM STROKE (IP 67 & 400 VOLTE)', 'IRS POINT MACHINE 220MM STROKE (IP 67 & 400 VOLTE)'),
    ('POWER SUPPLY FOR ELECTRONIC INTERLOCKING VDU', 'POWER SUPPLY FOR ELECTRONIC INTERLOCKING VDU'),
    ('FENCING FRAMES FOR GRS APP CASE', 'FENCING FRAMES FOR GRS APP CASE'),
    ('GRS APP CASE (FULL) COATED WITH HEAT RESISTANT PAINT', 'GRS APP CASE (FULL) COATED WITH HEAT RESISTANT PAINT'),
    ('SPECIAL SPANNER FOR IRS POINT M/C GROUND CONNECTION', 'SPECIAL SPANNER FOR IRS POINT M/C GROUND CONNECTION'),
    ('SPRING TENSION ADJUSTOR FOR DLBI', 'SPRING TENSION ADJUSTOR FOR DLBI'),
    ('THUMB SWITCH 2 POSITION', 'THUMB SWITCH 2 POSITION'),
    ('THUMB SWITCH 3 POSITION', 'THUMB SWITCH 3 POSITION'),
    ('PUSH SWITCH FOR LC GATE PANEL', 'PUSH SWITCH FOR LC GATE PANEL'),
    ('KNOB FOR CONTROL PANEL', 'KNOB FOR CONTROL PANEL'),
    ('GALVANISED GROUND CONNECTION FOR 220MM STROKE', 'GALVANISED GROUND CONNECTION FOR 220MM STROKE'),
    ('GALVANISED COVER FOR IRS POINT MACHINE', 'GALVANISED COVER FOR IRS POINT MACHINE'),
    ('POINT TESTING GAUGE', 'POINT TESTING GAUGE'),
    ('MS BOX FOR LC GATE SWITCH', 'MS BOX FOR LC GATE SWITCH'),
    ('TIPSS', 'TIPSS'),
    ('OPERATING PANEL FOR EOLB GATE', 'OPERATING PANEL FOR EOLB GATE'),
    ('GROUND CONNECTION FOR IRS POINT MACHINE 220MM STROKE 54 1 IN 85 LAYOUT)', 'GROUND CONNECTION FOR IRS POINT MACHINE 220MM STROKE 54 1 IN 85 LAYOUT)'),
    ('FRP MAKE MAIN SIGNALING UNIT (3 ASPECTS)', 'FRP MAKE MAIN SIGNALING UNIT (3 ASPECTS)'),
    ('FRP MAKE MAIN SIGNALING UNIT (4 ASPECTS)', 'FRP MAKE MAIN SIGNALING UNIT (4 ASPECTS)'),
)
'''