from .models import *
from rest_framework import serializers

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'full_name', 'email', 
                  'phone_number', 'rent_amount', 
                  'has_paid', 'move_in', 'move_out']
        
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'city', 'state', 'flat_available']
        
        
class FlatSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    property = PropertySerializer(read_only=True)
    class Meta:
        model = Flat
        fields = ['id', 'tenant', 'property', 'flat_number']
        
class AddFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['id', 'tenant', 'property', 'flat_number']
        
        
class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = ['id', 'flat', 'lease_agreement']