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

class Automobile_view(viewsets.ModelViewSet):
    queryset = Automobile.objects.all()
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
        if datos['picture_trunk'] == '':
            datos.pop('picture_trunk')
        if datos['picture_profile'] == '':
            datos.pop('picture_profile')
        if datos['picture_motor'] == '':
            datos.pop('picture_motor')
        if datos['picture_dashboard'] == '':
            datos.pop('picture_dashboard')
        if datos['picture_back_seats'] == '':
            datos.pop('picture_back_seats')
        serializer = self.get_serializer(instance, data=datos, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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