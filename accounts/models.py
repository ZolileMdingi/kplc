from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    idtype = models.CharField(max_length=200, null=True, blank=True)
    idnum = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    pobox = models.CharField(max_length=200, null=True, blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    constituency = models.CharField(max_length=200, null=True, blank=True)
    ward = models.CharField(max_length=200, null=True, blank=True)
    lr_num = models.CharField(max_length=200, null=True, blank=True)
    estate_village = models.CharField(max_length=200, null=True, blank=True)
    duplicate = models.CharField(max_length=200, null=True, blank=True)
    vcode = models.CharField(max_length=200, null=True, blank=True)
    ccp = models.CharField(max_length=200, null=True, blank=True) #customer contract persomn
    voltage = models.CharField(max_length=200, null=True, blank=True)
    connetype = models.CharField(max_length=200, null=True, blank=True)
    connedate = models.CharField(max_length=200, null=True, blank=True)
    amd = models.CharField(max_length=200, null=True, blank=True) #authorised max demand
    profile_pic = models.FileField(null=True, blank=True) #id
    pincertificate = models.FileField(null=True, blank=True)
    td = models.FileField(null=True, blank=True) #titile deed
    wc = models.FileField(null=True, blank=True) #wiring certificate
    
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = (
        ('Standard Application', 'Standard Application'),
        ('Premium Application', 'Premium Application'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

    
#class Appliance(models.Model):
#    APPLIANCES = (
#        ('Kettle', 'Kettle'),
#        ('Fridge', 'Fridge'),
#        ('TV', 'TV'),
#        ('Other', 'Other'),
#    )
#    
#    appliancename = models.CharField(max_length=200, null=True, blank=True, choices=APPLIANCES)
#    consumption = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
#    units = models.CharField(max_length=200, default="Kwh", null=True, blank=True)
#    num_appliances = models.IntegerField(null=True, blank=True)
#    total = models.IntegerField(null=True, blank=True)
#    
#    def __str__(self):
#        return self.appliance
#    
#    
class Order(models.Model):
    STATUS = (
        ('Standard Application', 'Standard Application'),
        ('Premium Application', 'Premium Application'),
        
    )
    AGREESTATUS = (
        ('YES I AGREE', 'YES I AGREE'),
        ('NO I DO NOT AGREE', 'NO I DO NOT AGREE'),
        
    )
    APPSTATUS = (
        ('Under Review', 'Under Review'),
        ('Waiting for Qoute', 'Waiting for Qoute'),
        ('On Design', 'On Design'),
        ('Site visited', 'Site visited'),
        ('Installed', 'Installed'),
        
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS) #Plan Standard or Premium
    loc = models.CharField(max_length=200, null=True, blank=True) #location cordinates
    appstatus = models.CharField(max_length=200, default="Under Review", null=True, blank=True) #application status
    appnum = models.CharField(max_length=200, null=True, blank=True) #application number
    siteinfo = models.CharField(max_length=200, null=True, blank=True) #site information
    agreebtn = models.CharField(max_length=200, null=True, blank=True, choices=AGREESTATUS)
    agreewayleave = models.CharField(max_length=200, null=True, blank=True, choices=AGREESTATUS)
    qoutation = models.FileField(null=True, blank=True)
    appcontrol = models.CharField(max_length=200, default="busdevclerk", null=True, blank=True) #To note what has been done to the application
    installnote = models.CharField(max_length=400, null=True, blank=True) #Engineer intallation note
    proposal = models.FileField(null=True, blank=True)
    maplatlon = models.CharField(max_length=400, null=True, blank=True) #The map coordinates
    payment = models.FileField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name
    
