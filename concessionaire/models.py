from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Business(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.name
#AbstractUser
class Employee(AbstractUser):
    business = models.ForeignKey(Business, on_delete=models.PROTECT,default=1)
    id_employee = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    token = models.CharField(max_length=100,null=True,blank=True,default='')
    def __str__(self):
        return self.id_employee

class Automobile(models.Model):
    OPTIONS_TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Auto', 'Auto'),
    ]
    OPTIONS_FUEL = [
        ('Gasoline','Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    OPTIONS_TRACTION =[
        ('4WD','4WD'),
        ('AWD', 'AWD'),
        ('FWD', 'FWD'),
        ('RWD', 'RWD'),
    ]
    TITLE_STATUS_OPTION = [
        ('Clean','Clean'),
        ('Rebuild/Reconstructed','Rebuild/Reconstructed'),
    ]
    BODY_SHAPE =[
        ('Sedan','Sedan'),
        ('Coupe','Coupe'),
        ('Hatchback','Hatchback'),
        ('Cabriolet','Cabriolet'),
        ('Pickup','Pickup'),
        ('Wagon','Wagon'),
        ('Van','Van'),
        ('SUV','SUV'),
    ]
    MATERIALS = [
        ('Leather','Leather'),
        ('Cloth','Cloth'),
    ]
    brand = models.CharField(max_length=50)#
    mileage = models.FloatField()#
    price = models.FloatField()#
    model = models.CharField(max_length=30)#
    year = models.CharField(max_length=50)#
    id_vehicle = models.IntegerField()#
    in_promotion = models.BooleanField(default=False)
    description = models.TextField()#
    owners = models.CharField(max_length=50,default='')#
    picture_main = models.ImageField(upload_to='automobile/')#
    picture_front = models.ImageField(upload_to='automobile/')#
    picture_back = models.ImageField(upload_to='automobile/')#
    picture_profile = models.ImageField(upload_to='automobile/')#
    picture_engine = models.ImageField(upload_to='automobile/')#
    picture_dashboard = models.ImageField(upload_to='automobile/')#
    main_collage = models.ImageField(upload_to='automobile/')#
    exterior_color = models.CharField(max_length=50)#
    interior_color = models.CharField(max_length=50)#
    VIN = models.CharField(max_length=50)#
    capacity = models.IntegerField(default=5)#
    engine_size = models.CharField(max_length=50)  #
    accidents = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)#


    body_shape = models.CharField(max_length=50, choices=BODY_SHAPE, default='Sedan')  #
    transmission = models.CharField(max_length=20,choices=OPTIONS_TRANSMISSION, default='Manual')#
    title_status = models.CharField(max_length=50,choices=TITLE_STATUS_OPTION, default='Clean')#
    traction = models.CharField(max_length=50, choices=OPTIONS_TRACTION, default='4WD')#
    fuel = models.CharField(max_length=20, choices=OPTIONS_FUEL, default='Gasoline')
    seats_materials = models.CharField(max_length=20, choices=MATERIALS, default='Leather')


    electric_parking_brake = models.BooleanField(default=False)#
    power_seats = models.BooleanField(default=False)#
    reverse_camera = models.BooleanField(default=False)#
    reversing_sensors = models.BooleanField(default=False)#
    navigation_system = models.BooleanField(default=False)#
    moonroof = models.BooleanField(default=False)#
    def __str__(self):
        return self.id_vehicle

class Inventory(models.Model):
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    automobile = models.ForeignKey(Automobile, on_delete=models.PROTECT)
    amount = models.IntegerField()
    def __str__(self):
        return self.amount

class Promotion(models.Model):
    durations = models.TimeField()
    new_price = models.FloatField()
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    def __str__(self):
        return self.new_price







