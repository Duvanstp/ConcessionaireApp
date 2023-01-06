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
    OPTIONS =[
        ('High-end', 'High-end'),
        ('Mid-range', 'Mid-range'),
        ('Low end', 'Low end'),
    ]
    brand = models.CharField(max_length=30)
    price = models.FloatField()
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    id_vehicle = models.IntegerField()
    in_promotion = models.BooleanField(default=False)
    description = models.TextField()
    details = models.TextField()
    range = models.CharField(max_length=10, choices=OPTIONS, default='Low end')
    plates = models.CharField(max_length=50)
    picture_main = models.ImageField(upload_to='automobile/')
    picture_front = models.ImageField(upload_to='automobile/')
    picture_back = models.ImageField(upload_to='automobile/')
    picture_trunk = models.ImageField(upload_to='automobile/')
    picture_profile = models.ImageField(upload_to='automobile/')
    picture_motor = models.ImageField(upload_to='automobile/')
    picture_dashboard = models.ImageField(upload_to='automobile/')
    picture_back_seats= models.ImageField(upload_to='automobile/')
    color = models.CharField(max_length=50)
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







