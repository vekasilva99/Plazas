from django.db import models

# Create your models here.
class Store (models.Model):
    id_store=models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    max_capacity = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Warehouse (models.Model):
    id_warehouse=models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    max_capacity = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Product (models.Model):
    id_product=models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Category (models.Model):
    id_category=models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Client (models.Model):
    id_client=models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Affiliate (models.Model):
    id_client=models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    identification = models.CharField(max_length=30, null=True)
    points = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name