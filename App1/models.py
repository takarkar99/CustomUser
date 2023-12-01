from django.db import models
from CustomizeUser.models import CustomUser

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    CustomUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.CustomUser


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=250)
    price = models.FloatField()
    

    def __str__(self):
        return self.product_name
    

    def update_product_name(self, new_product_name):
        self.product_id = new_product_name
        self.save()


    @classmethod
    def update_price(cls,product_id,new_price):
        obj =  cls.objects.get(product_id=product_id)
        obj.price = new_price
        obj.save()
    

    def product_value_limit(quanlity):
        obj = Product.objects.all()[:quanlity]

        return obj

        

status_choice = [
    (1, 'Not packed'),
    (2, 'Ready For Shipment'),
    (3, 'Shipped'),
    (4, 'Delivered')
    ]

class Productincard(models.Model):
    
    class Meta:
        unique_together = (('card', 'product'),)
    product_in_card_id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.card}-{self.product}"



class Order(models.Model):

    CustomUser = models.ManyToManyField(CustomUser)
    status = models.IntegerField(choices=status_choice, default=1)