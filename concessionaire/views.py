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

class Post_view(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post_serializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['img_main'] == '':
            datos.pop('img_main')
        if datos['img_seccion_1'] == '':
            datos.pop('img_seccion_1')
        if datos['img_seccion_2'] == '':
            datos.pop('img_seccion_2')
        if datos['img_seccion_3'] == '':
            datos.pop('img_seccion_3')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class Home_view(viewsets.ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = Automobile_serializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['main_view'] == '':
            datos.pop('main_view')
        if datos['front_view'] == '':
            datos.pop('front_view')
        if datos['back_view'] == '':
            datos.pop('back_view')
        if datos['profile_view'] == '':
            datos.pop('profile_view')
        if datos['engine_view'] == '':
            datos.pop('engine_view')
        if datos['dashboard_view'] == '':
            datos.pop('dashboard_view')
        if datos['gallery'] == '':
            datos.pop('gallery')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['main_view'] == '':
            datos.pop('main_view')
        if datos['front_view'] == '':
            datos.pop('front_view')
        if datos['back_view'] == '':
            datos.pop('back_view')
        if datos['profile_view'] == '':
            datos.pop('profile_view')
        if datos['engine_view'] == '':
            datos.pop('engine_view')
        if datos['dashboard_view'] == '':
            datos.pop('dashboard_view')
        if datos['gallery'] == '':
            datos.pop('gallery')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        datos = request.data.copy()
        if datos['main_view'] == '':
            datos.pop('main_view')
        if datos['front_view'] == '':
            datos.pop('front_view')
        if datos['back_view'] == '':
            datos.pop('back_view')
        if datos['profile_view'] == '':
            datos.pop('profile_view')
        if datos['engine_view'] == '':
            datos.pop('engine_view')
        if datos['dashboard_view'] == '':
            datos.pop('dashboard_view')
        if datos['gallery'] == '':
            datos.pop('gallery')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
class Automobile_view(viewsets.ModelViewSet): #STORE
#    queryset = Automobile.objects.all()
    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        exterior_color = self.request.query_params.get('exterior_color')
        price = self.request.query_params.get('price')
        if brand:
            queryset = Automobile.objects.filter(brand=brand).values()
        elif brand and exterior_color:
            queryset = Automobile.objects.filter(brand=brand, exterior_color=exterior_color).values()
        elif brand and price:
            queryset = Automobile.objects.filter(brand=brand, price__lte=price).values()
        elif brand and exterior_color and price:
            queryset = Automobile.objects.filter(brand=brand, exterior_color=exterior_color, price__lte=price).values()
        elif exterior_color:
            queryset = Automobile.objects.filter(exterior_color=exterior_color).values()
        elif exterior_color and price:
            queryset = Automobile.objects.filter(exterior_color=exterior_color, price__lte=price).values()
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
        if datos['main_view'] == '':
            datos.pop('main_view')
        if datos['front_view'] == '':
            datos.pop('front_view')
        if datos['back_view'] == '':
            datos.pop('back_view')
        if datos['profile_view'] == '':
            datos.pop('profile_view')
        if datos['engine_view'] == '':
            datos.pop('engine_view')
        if datos['dashboard_view'] == '':
            datos.pop('dashboard_view')
        if datos['gallery'] == '':
            datos.pop('gallery')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)