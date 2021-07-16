from django.db import  models
# Classe contenant l'objet catégorie
class Category(models.Model):
    name = models.CharField(max_length=20)
# Methode de classe pour reccuperer tous les objets de ma classe
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

# Construction de la classe pour affecter automatique le nom de chaque catégorie créee en label coté admin
    def __str__(self):
        return self.name
