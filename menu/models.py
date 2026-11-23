from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    orders_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    status = models.CharField(max_length=20,choices=STATUS,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.total_price = self.dish.price * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return self.user.username