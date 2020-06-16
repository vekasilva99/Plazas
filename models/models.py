from django.db import models

# Create your models here.
class Store (models.Model):
    id_store=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    max_capacity = models.IntegerField()
    openingHour  = models.TimeField()
    closingHour = models.TimeField()
    def __str__(self):
        return self.name

class Warehouse (models.Model):
    id_warehouse=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    max_capacity = models.IntegerField()
    id_store=models.OneToOneField(
        'Store', on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.name

class Product (models.Model):
    id_product=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    id_category=models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class Category (models.Model):
    id_category=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Client (models.Model):
    GENDER = ('F', ('Femenine')), ('M', ('Masculine'))
    id_client=models.CharField(max_length=10, primary_key=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=False, null=False)
    def __str__(self):
        return self.id_client

class Affiliate (models.Model):
    id_client=models.models.OneToOneField(
        'Client', on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=30, null=True)
    identification = models.CharField(max_length=8, unique=True)
    points = models.Integer(default=0)
    def __str__(self):
        return self.name

class Employee (models.Model):
    GENDER = ('F', ('Femenine')), ('M', ('Masculine'))
    id_employee=models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, null=True)
    identification = models.CharField(max_length=8, unique=True)
    salary = models.IntegerField()
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=False, null=False)
    id_store=models.ForeignKey(Store, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class Visit (models.Model):
    class Meta:
        unique_together = (('id_client', 'date','hour'),)
    id_client=models.ForeignKey(Client, on_delete= models.CASCADE)
    id_store=models.ForeignKey(Store, on_delete= models.CASCADE)
    hour=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.id_client

class Bank (models.Model):
    id_bank=models.CharField(max_length=2, primary_key=True)
    name=models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Cost (models.Model): 
    class Meta:
        unique_together = (('id_product', 'date'),)
    id_product=models.ForeignKey(Product, on_delete= models.CASCADE)
    date=models.DateField()
    cost=models.IntegerField()
    def __str__(self):
        return self.id_product

class Shelf (models.Model): 
    class Meta:
        unique_together = (('id_store', 'id_shelf'),)
    id_store=models.ForeignKey(Store, on_delete= models.CASCADE)
    id_product=models.ForeignKey(Product, on_delete= models.CASCADE)
    id_shelf=models.IntegerField()
    max_capacity=models.IntegerField()

    def __str__(self):
        return self.name

class Shelf_Quantity (models.Model): 
    class Meta:
        unique_together = (('id_store', 'id_shelf'),)
    id_store=models.ForeignKey(Store, on_delete= models.CASCADE)
    id_shelf=models.ForeignKey(Shelf, on_delete= models.CASCADE)
    quantity=models.IntegerField()
    hour=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.name

class Bill (models.Model): 
    id_bill=models.AutoField(primary_key=True)
    id_client=models.ForeignKey(Client, on_delete= models.CASCADE)
    total_bs=models.FloatField()
    points=models.IntegerField()
    hour=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.name