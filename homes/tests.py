from .models import Tenant
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class TenantTest(TestCase):
    def setUp(self) :
        self.client = APIClient()
        
        self.create_tenant_url = ('/homes/tenants/')
        # Test data for tenant creation
        self.tenant_data =  {
            "full_name": "test",
            "email": "test@gmail.com",
            "phone_number": "0987654321",
            "rent_amount": 500000.0,
            "has_paid": False,
            "move_in": "2023-07-29",
        }
        
    def test_create_tenant(self):
        response = self.client.post(self.create_tenant_url, self.tenant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    
    def test_update_tenant(self):
        tenant_id = Tenant.objects.get(full_name='test').id
        self.update_tenant_url = reverse('tenant-detail', args=[tenant_id])  # Use reverse to get the URL for updating the tenant

        self.updated_tenant_profile = {
            "full_name": "test1",
            "email": "test1@gmail.com"
        }

        response = self.client.put(self.update_tenant_url, self.updated_tenant_profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], self.updated_tenant_profile['full_name'])
        self.assertEqual(response.data['email'], self.updated_tenant_profile['email'])



