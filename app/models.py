import uuid

from django.db import models

# Create your models here.


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(
        'product', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    company_id = models.ForeignKey(
        'company', on_delete=models.CASCADE, related_name='company_id')

    class Meta:
        verbose_name = 'Produto'

    def __str__(self):
        return self.name


class Transations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoicing = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'transações'

    def __str__(self):
        return self.id


class Companyowner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='company')
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Proprietário'

    def __str__(self):
        return self.name


class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.name
