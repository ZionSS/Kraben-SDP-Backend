from cgi import print_exception
from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appusers')
    USER_TYPES = (
        ('C', 'Customer'),
        ('S', 'Seller')
    )
    user_type = models.CharField(max_length=1,choices=USER_TYPES, default='C')
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    district = models.CharField(max_length=30, null=True, blank=True)
    province = models.CharField(max_length=30, null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.email +" "+self.first_name

class OrderItem(models.Model):
    product_id = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return self.product_id


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    def __str__(self):
        return self.user_id

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    STATUS = ((
        ('P', 'Pending'),
        ('C', 'Confirmed')
    ))
    status = models.CharField(max_length=1,choices=STATUS)
    
    def __str__(self):
        return self.user_id

class Product(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    amount = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.title
    '''shop'''