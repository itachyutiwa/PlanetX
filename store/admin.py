from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.contrib.admin import AdminSite



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer )
admin.site.register(Order )

class StoreAdminSite(AdminSite):
    site_header = "PlanetX"
    site_title = "PanetX, Boutique en ligne"
    index_title = "Bienvenue sur la boutique en ligne, PlanetX"



