from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

class Hotel(TenantMixin, models.Model):
    name = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    stars = models.IntegerField()
    email = models.TextField(blank=True)
    primary_color = models.CharField(max_length=7, default='#FFFFFF')  # Default to white
    secondary_color = models.CharField(max_length=7, default='#000000')  # Default to black

    auto_create_schema= True

    def __str__(self):
        return self.name

class HotelDomain(DomainMixin):
    pass

