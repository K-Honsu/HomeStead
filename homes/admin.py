from django.contrib import admin
from .models import Tenant, Property, Flat, Lease

admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Flat)
admin.site.register(Lease)
