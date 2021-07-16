from django.db import  models
from django.core.validators import MinLengthValidator
# Classe contenant notre objet client(Customer)
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
# Methode pour enregistrer chaque client
    def register(self):
        self.save()
# Methode pour recuperer un client par son adresse e-mail
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

# Methode pour vérifier si le mail recherché existe bien
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False


