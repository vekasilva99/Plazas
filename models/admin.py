from django.contrib import admin
from .models import Store, Warehouse, Category, Product, Client, Affiliate, Employee, Visit, Bank, Cost, Shelf, Shelf_Quantity, Bill, Bill_Detail, Stored_in
# Register your models here.

admin.site.register(Store)
admin.site.register(Warehouse)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Affiliate)
admin.site.register(Employee)
admin.site.register(Visit)
admin.site.register(Bank)
admin.site.register(Cost)
admin.site.register(Shelf)
admin.site.register(Shelf_Quantity)
admin.site.register(Bill)
admin.site.register(Bill_Detail)
admin.site.register(Stored_in)

