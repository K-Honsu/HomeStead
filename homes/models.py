from django.db import models

class Tenant(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    rent_amount = models.DecimalField(decimal_places=2, max_digits=9)
    has_paid = models.BooleanField(default=False)
    move_in = models.DateField()
    move_out = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.full_name} is now a tenant'
    

class Property(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    flat_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name} property, located at {self.address}'
    
    
class Flat(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenants')
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, related_name='properties')
    flat_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.tenant} is occuping flat number {self.flat_number} at {self.property}'
    
    
class Lease(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.DO_NOTHING, related_name='lease')
    lease_agreement = models.FileField(upload_to='files')
    
    def __str__(self) -> str:
        return f'{self.lease_agreement} for {self.flat}'
