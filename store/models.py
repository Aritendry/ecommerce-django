from django.db import models
from shop.settings import AUTH_USER_MODEL
# Create your models here.



"""
Product
-Nom(champ de text)
-Slug(champ de text)
-Prix(interger , float)
-Quantite(integer)
-Description(champ de text)
-Image

"""
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=500 , blank=True)
    thumbnail = models.ImageField(upload_to='products' , blank=True , null=True)


    #qui permettra d'afficher le nom du produit dans la bd
    def __str__(self):
        return f"{self.name}  ({self.quantity})"
    

#Article (order)
""" 
- Utilisateur
- Produit
- Quantite
- Commandé ou non
"""

class Order(models.Model):
    
    #Plusieurs produit relier a un utilisateur
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name}  ({self.quantity})"

#Cart 
""" 
- Utilisateur
- Articles
- Commande ou non
- Date de la commande
"""
class Cart(models.Model):

    #Plusieur article relier a un utilisateur , donc un utilisateur a une seule panier
    user = models.OneToOneField(AUTH_USER_MODEL , on_delete=models.CASCADE)
    #Plusieur commande relier a un utilisateur ou  un panier
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True , null=True)

    def __str__(self):
        return self.user.username