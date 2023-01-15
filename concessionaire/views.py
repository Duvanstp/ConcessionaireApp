from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from concessionaire.serializers import *
from concessionaire.models import *
# Create your views here.
class Business_view(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = Business_serializer

class Employee_view(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_serializer

class Inventory_view(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = Inventory_serializer

class Promotion_view(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = Promotion_serializer

class TokenProvider(ObtainAuthToken):
    def post(self,  request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        employee = Employee_serializer(user)
        return Response(employee.data)

class Home_view(viewsets.ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = Automobile_serializer

class User_interface_view(viewsets.ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = Automobile_serializer
class Automobile_brand_view(viewsets.ModelViewSet): #Brand
    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        if brand:
            queryset = Automobile.objects.filter(brand=brand)
        else:
            queryset = Automobile.objects.all()
        return queryset
    serializer_class = Automobile_serializer

class Comparison_automobile_view(viewsets.ModelViewSet):
    def get_queryset(self):
        id1 = self.request.query_params.get('id1')
        id2 = self.request.query_params.get('id2')
        if id1 and id2:
            queryset = Automobile.objects.filter(id=id1).values() | Automobile.objects.filter(id=id2).values()
        elif id1:
            queryset = Automobile.objects.all()
        elif id2:
            queryset = Automobile.objects.all()
        else:
            queryset = Automobile.objects.all()
        return queryset
    serializer_class = Automobile_serializer
class Automobile_view(viewsets.ModelViewSet): #STORE
#    queryset = Automobile.objects.all()
    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        color = self.request.query_params.get('color')
        price = self.request.query_params.get('price')
        if brand:
            queryset = Automobile.objects.filter(brand=brand).values()
        elif brand and color:
            queryset = Automobile.objects.filter(brand=brand, color=color).values()
        elif brand and price:
            queryset = Automobile.objects.filter(brand=brand, price__lte=price).values()
        elif brand and color and price:
            queryset = Automobile.objects.filter(brand=brand, color=color, price__lte=price).values()
        elif color:
            queryset = Automobile.objects.filter(color=color).values()
        elif color and price:
            queryset = Automobile.objects.filter(color=color, price__lte=price).values
        elif price:
            queryset = Automobile.objects.filter(price__lte=price)
        else:
            queryset = Automobile.objects.all()
        return queryset
    serializer_class = Automobile_serializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['picture_main'] == '':
            datos.pop('picture_main')
        if datos['picture_front'] == '':
            datos.pop('picture_front')
        if datos['picture_back'] == '':
            datos.pop('picture_back')
        if datos['picture_profile'] == '':
            datos.pop('picture_profile')
        if datos['picture_motor'] == '':
            datos.pop('picture_motor')
        if datos['picture_dashboard'] == '':
            datos.pop('picture_dashboard')
        if datos['main_collage']=='':
            datos.pop('main_collage')
        if datos['data_sheet']=='':
            datos.pop('data_sheet')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)