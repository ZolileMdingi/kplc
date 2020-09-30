from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    COUNTIES = [
        ("Mombasa","Mombasa"),
        ("Kwale","Kwale"),
        ("Kilifi","Kilifi"),
        ("Tana River","Tana River"),
        ("Tana River","Tana River"),
        ("Taita Taveta","Taita Taveta")
    ]
    WARDS = [
        ( "CHAANI","CHAANI"),
        ( "MIRITINI","MIRITINI"),
        ( "AIRPORT","AIRPORT"),
        ( "PORT REITZ","PORT REITZ"),
        ( "KIPEVU","KIPEVU"),
        ( "JOMVU KUU","JOMVU KUU"),
        ( "MAGONGO","MAGONGO"),
        ( "MIKINDANI","MIKINDANI"),
        ( "SHANZU","SHANZU"),
        ( "MWAKIRUNGE","MWAKIRUNGE"),
        ( "MJAMBERE","MJAMBERE"),
        ( "MAGOGONI","MAGOGONI"),
        ( "JUNDA","JUNDA"),
        ( "MTOPANGA","MTOPANGA"),
        ( "BAMBURI","BAMBURI"),
        ( "MKOMANI","MKOMANI"),
        ( "KONGOWEA","KONGOWEA"),
        ( "KADZANDANI","KADZANDANI"),
        ( "ZIWA LA NG'OMBE","ZIWA LA NG'OMBE"),
        ( "FRERE TOWN","FRERE TOWN"),
        ( "MTONGWE","MTONGWE"),
        ( "TIMBWANI","TIMBWANI"),
        ( "BOFU","BOFU"),
        ( "LIKONI","LIKONI"),
        ( "SHIKA ADABU","SHIKA ADABU"),
        ( "MJI WA KALE/ MAKADARA","MJI WA KALE/ MAKADARA"),
        ( "TUDOR","TUDOR"),
        ( "TONONOKA","TONONOKA"),
        ( "SHIMANZI/ GANJONI","SHIMANZI/ GANJONI"),
        ( "MAJENGO","MAJENGO"),
        ( "RAMISI","RAMISI"),
        ( "GOMBATO BONGWE","GOMBATO BONGWE"),
        ( "UKUNDA","UKUNDA"),
        ( "KINONDO","KINONDO"),
        ( "PONGWE KIDIMU/KIGWEDE","PONGWE KIDIMU/KIGWEDE"),
        ( "VANGA","VANGA"),
        ( "MWERENI","MWERENI"),
        ( "DZOMBO","DZOMBO"),
        ( "KUBO SOUTH","KUBO SOUTH"),
        ( "MKONGANI","MKONGANI"),
        ( "TSIMBA GOLINI","TSIMBA GOLINI"),
        ( "TIWI","TIWI"),
        ( "WAA","WAA"),
        ( "MACKINON ROAD","MACKINON ROAD"),
        ( "NDAVAYA","NDAVAYA"),
        ( "PUMA","PUMA"),
        ( "KINANGO","KINANGO"),
        ( "KASEMENI","KASEMENI"),
        ( "MWAVUMBO","MWAVUMBO"),
        ( "CHENGONI/SAMBURU","CHENGONI/SAMBURU"),
        ( "MATSANGONI","MATSANGONI"),
        ( "MNARANI","MNARANI"),
        ( "SOKONI","SOKONI"),
        ( "TEZO","TEZO"),
        ( "KIBARANI","KIBARANI"),
        ( "WATAMU","WATAMU"),
        ( "DABASO","DABASO"),
        ( "JUNJU","JUNJU"),
        ( "SHIMO LA TEWA","SHIMO LA TEWA"),
        ( "MTEPENI","MTEPENI"),
        ( "CHASIMBA","CHASIMBA"),
        ( "MWARAKAYA","MWARAKAYA"),
        ( "KAYAFUNGO","KAYAFUNGO"),
        ( "MARIAKANI","MARIAKANI"),
        ( "MWANAMWINGA","MWANAMWINGA"),
        ( "KALOLENI","KALOLENI"),
        ( "JIBANA/KAMBE/RIBE","JIBANA/KAMBE/RIBE"),
        ( "MAZERASRABAI/KISURUTINI","MAZERASRABAI/KISURUTINI"),
        ( "MWAWESA","MWAWESA"),
        ( "RURUMA","RURUMA"),
        ( "SOKOKE","SOKOKE"),
        ( "BAMBA","BAMBA"),
        ( "JARIBUNI","JARIBUNI"),
        ( "DUNGICHA/ GANZE","DUNGICHA/ GANZE"),
        ( "JILORE","JILORE"),
        ( "GANDA","GANDA"),
        ( "KAKUYUNI","KAKUYUNI"),
        ( "SHELLA","SHELLA"),
        ( "MALINDI TOWN","MALINDI TOWN"),
        ( "ADU","ADU"),
        ( "MARAFA","MARAFA"),
        ( "SABAKI","SABAKI"),
        ( "MAGARINI","MAGARINI"),
        ( "GONGONI","GONGONI"),
        ( "GARASHI","GARASHI"),
        ( "GARSEN NORTH","GARSEN NORTH"),
        ( "GARSEN WEST","GARSEN WEST"),
        ( "GARSEN CENTRAL","GARSEN CENTRAL"),
        ( "KIPINI EAST","KIPINI EAST"),
        ( "GARSEN SOUTH","GARSEN SOUTH"),
        ( "KIPINI WEST","KIPINI WEST"),
        ( "CHEWANI","CHEWANI"),
        ( "KINAKOMBA","KINAKOMBA"),
        ( "MAKINDUNI","MAKINDUNI"),
        ( "WAYU","WAYU"),
        ( "BANGALE","BANGALE"),
        ( "CHEWELE","CHEWELE"),
        ( "HIRIMAN","HIRIMAN"),
        ( "MADOGO","MADOGO"),
        ( "SALA","SALA"),
        ( "KIUNGA","KIUNGA"),
        ( "BASUBA","BASUBA"),
        ( "FAZA","FAZA"),
        ( "MKOMANI","MKOMANI"),
        ( "SHELLA","SHELLA"),
        ( "WITU","WITU"),
        ( "HINDI","HINDI"),
        ( "HONGWE","HONGWE"),
        ( "BAHARI","BAHARI"),
        ( "MKUNUMBI","MKUNUMBI"),
        ( "MATA","MATA"),
        ( "MAHOO","MAHOO"),
        ( "MBOGHONI","MBOGHONI"),
        ( "CHALA","CHALA"),
        ( "BOMANI","BOMANI"),
        ( "MWANDA/MGANGE","MWANDA/MGANGE"),
        ( "KISHUSHE/WUMINGU","KISHUSHE/WUMINGU"),
        ( "WERUGHA","WERUGHA"),
        ( "WUNDANYI/MBALE","WUNDANYI/MBALE"),
        ( "CHAWIA","CHAWIA"),
        ( "BURA","BURA"),
        ( "WUSI/KISHAMBA","WUSI/KISHAMBA"),
        ( "RONGE","RONGE"),
        ( "MWATATE","MWATATE"),
        ( "NGOLIA","NGOLIA"),
        ( "KASIGAU","KASIGAU"),
        ( "MARUNGU","MARUNGU"),
        ( "SAGALA","SAGALA"),
        ( "MBOLOLO","MBOLOLO"),
        ( "KALOLENI","KALOLENI"),
    ]
    CONSTITUENCIES = [
        ( "Changamwe","Changamwe"),
        ( "Jomvu","Jomvu"),
        ( "Kisauni","Kisauni"),
        ( "Nyali","Nyali"),
        ( "Likoni","Likoni"),
        ( "Mvita","Mvita"),
        ( "Msambweni","Msambweni"),
        ( "Lunga Lunga","Lunga Lunga"),
        ( "Matuga","Matuga"),
        ( "Kinango","Kinango"),
        ( "Kilifi North","Kilifi North"),
        ( "Kilifi South","Kilifi South"),
        ( "Kaloleni","Kaloleni"),
        ( "Rabai","Rabai"),
        ( "Ganze","Ganze"),
        ( "Malindi","Malindi"),
        ( "Magarini","Magarini"),
        ( "Garsen","Garsen"),
        ( "Galole","Galole"),
        ( "Bura","Bura"),
        ( "Lamu East","Lamu East"),
        ( "Lamu West","Lamu West"),
        ( "Taveta","Taveta"),
        ( "Wundanyi","Wundanyi"),
        ( "Mwatate","Mwatate"),
        ( "Voi","Voi")

    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    idtype = models.CharField(max_length=200, null=True, blank=True)
    idnum = models.CharField(max_length=200, null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True,  choices=COUNTIES)
    pobox = models.CharField(max_length=200, null=True, blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    constituency = models.CharField(max_length=200, null=True, choices=CONSTITUENCIES)
    ward = models.CharField(max_length=200, null=True, choices=WARDS)
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
    
