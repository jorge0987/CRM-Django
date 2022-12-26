from django.contrib import admin

from .models import Clients, Company, Companyowner, Product, Transations

# Register your models here.

admin.site.register(Company)
admin.site.register(Companyowner)
admin.site.register(Product)
admin.site.register(Transations)
admin.site.register(Clients)
