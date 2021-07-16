from django.db import models
from .product import Product
from .customer import Customer
import datetime

# Classe contenant notre cobjet commande
class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
# Methode pour definir un champ grisé pour aider les utilisateurs
    def placeOrder(self):
        self.save()
# Methode pour récuperer un client par son adresse e-mail
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    def __str__(self):
        return "Date : {} ,contact client: {}".format(self.date,self.phone)

