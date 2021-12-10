import uuid

from django.db import models
from django.db.models import Sum
from django.conf import Settings

from product.models import Product

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    def generate_order_number(self):
        return uuid.uuid4()

    def save(self, *args, **kwargs):
        self.order_number = self._generate_order

        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(self, *args, **kwargs)

    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost =    
        else:
            self.delivery_cost = 0
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on-delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on-delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    self.lineitem_total = self.product.price * self.quantity
    super().save(*args, **kwargs)
