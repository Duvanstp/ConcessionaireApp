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
    OPTIONS_RANGE =[
        ('High-end', 'High-end'),
        ('Mid-range', 'Mid-range'),
        ('Low end', 'Low end'),
    ]
    OPTIONS_TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Auto', 'Auto'),
    ]
    OPTIONS_FUEL = [
        ('Gasoline','Gasoline'),
        ('Electric','Electric'),
        ('Hibrid','Hibrid'),
    ]
    OPTIONS_TRACTION =[
        ('4X2','4X2'),
        ('4X4','4X4'),
    ]
    body_shape = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    mileage = models.FloatField()
    price = models.FloatField()
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    id_vehicle = models.IntegerField()
    in_promotion = models.BooleanField(default=False)
    description = models.TextField()
    details = models.TextField()# no
    range = models.CharField(max_length=10, choices=OPTIONS_RANGE, default='Low end') #--
    plates = models.CharField(max_length=50)#--
    picture_main = models.ImageField(upload_to='automobile/')
    picture_front = models.ImageField(upload_to='automobile/')
    picture_back = models.ImageField(upload_to='automobile/')
    picture_profile = models.ImageField(upload_to='automobile/')
    picture_motor = models.ImageField(upload_to='automobile/')
    picture_dashboard = models.ImageField(upload_to='automobile/')
    color = models.CharField(max_length=50)
    ##
    main_collage = models.ImageField(upload_to='automobile/')
    capacity = models.IntegerField()
    transmission = models.CharField(max_length=20,choices=OPTIONS_TRANSMISSION, default='Manual')#-- pendiente de tener lista
    horsepower = models.CharField(max_length=50)
    airbag = models.BooleanField(default=False)
    traction = models.CharField(max_length=50, choices=OPTIONS_TRACTION, default='4X2') # 4x4 y 4x2 despleglable
    electric_parking_brake = models.BooleanField(default=False)
    electric_glasses = models.BooleanField(default=False)
    electric_mirrors = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    reverse_camera = models.BooleanField(default=False)
    reversing_sensors = models.CharField(max_length=100)
    electronic_stability_control = models.BooleanField(default=False)
    ascent_and_descent_control = models.BooleanField(default=False)
    data_sheet = models.FileField(upload_to='data_sheets/')
    forward_collision_alert = models.BooleanField(default=False)
    involuntary_lane_departure_alert = models.BooleanField(default=False)
    ABS = models.BooleanField(default=False)
    fuel = models.CharField(max_length=20,choices=OPTIONS_FUEL, default='Manual')
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







