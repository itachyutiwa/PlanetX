from django.db import models
from .category import Category


# Classe contenant notre produit
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
# Methode pour recuperer notre produit par son id
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)
# Methode pour recuperer tous les produit 
    @staticmethod
    def get_all_products():
        return Product.objects.all()
#Methode pour recuperer les produits par catégorie
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()