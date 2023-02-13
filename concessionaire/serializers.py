from rest_framework import serializers
from concessionaire.models import *
from drf_extra_fields.fields import Base64ImageField

class Business_serializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class Employee_serializer(serializers.ModelSerializer):
    business = Business_serializer(read_only=True)
    business_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Business.objects.all(), source='business')
    class Meta:
        model = Employee
        fields = '__all__'
    def create(self, validated_data):
        user = Employee(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class Automobile_serializer(serializers.ModelSerializer):
    main_view = Base64ImageField(required=False)
    front_view = Base64ImageField(required=False)
    back_view = Base64ImageField(required=False)
    profile_view = Base64ImageField(required=False)
    engine_view = Base64ImageField(required=False)
    dashboard_view = Base64ImageField(required=False)
    gallery = Base64ImageField(required=False)
    class Meta:
        model = Automobile
        fields = '__all__'

class Inventory_serializer(serializers.ModelSerializer):
    business = Business_serializer(read_only=True)
    business_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Business.objects.all(), source='business')
    automobile = Automobile_serializer(read_only=True)
    automobile_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Automobile.objects.all(),source='automobile')
    class Meta:
        model = Inventory
        fields = '__all__'

class Promotion_serializer(serializers.ModelSerializer):
    inventory = Business_serializer(read_only=True)
    inventory_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Inventory.objects.all(), source='inventory')
    class Meta:
        model = Promotion
        fields = '__all__'